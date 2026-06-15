# ─── Start All MCP Servers + Frontend ─────────────────────────────────────────
# Run this from the project root: .\scripts\start-all.ps1

Write-Host "Starting Unified Campus Intelligence Dashboard" -ForegroundColor Cyan
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor DarkGray

$projectRoot = Split-Path -Parent $PSScriptRoot

# Start MCP Servers
$servers = @(
    @{ Name = "Library";   Path = "$projectRoot\mcp-servers\library";   Port = 8001 },
    @{ Name = "Cafeteria"; Path = "$projectRoot\mcp-servers\cafeteria"; Port = 8002 },
    @{ Name = "Events";    Path = "$projectRoot\mcp-servers\events";    Port = 8003 },
    @{ Name = "Academics"; Path = "$projectRoot\mcp-servers\academics"; Port = 8004 }
)

$jobs = @()

foreach ($server in $servers) {
    Write-Host "Starting $($server.Name) MCP Server on port $($server.Port)..." -ForegroundColor Yellow
    $job = Start-Job -ScriptBlock {
        param($path, $port)
        Set-Location $path
        python server.py
    } -ArgumentList $server.Path, $server.Port
    $jobs += $job
    Start-Sleep -Milliseconds 500
}

Write-Host ""
Write-Host "All MCP Servers started!" -ForegroundColor Green
Write-Host ""

# Start Frontend
Write-Host "Starting Next.js Frontend..." -ForegroundColor Yellow
$frontendJob = Start-Job -ScriptBlock {
    param($path)
    Set-Location $path
    npm run dev
} -ArgumentList "$projectRoot\frontend"
$jobs += $frontendJob

Start-Sleep -Seconds 3

Write-Host ""
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor DarkGray
Write-Host "All services are running!" -ForegroundColor Green
Write-Host ""
Write-Host "  Library MCP:    http://localhost:8001" -ForegroundColor White
Write-Host "  Cafeteria MCP:  http://localhost:8002" -ForegroundColor White
Write-Host "  Events MCP:     http://localhost:8003" -ForegroundColor White
Write-Host "  Academics MCP:  http://localhost:8004" -ForegroundColor White
Write-Host "  Dashboard:      http://localhost:3000" -ForegroundColor Cyan
Write-Host ""
Write-Host "Press Ctrl+C to stop all services" -ForegroundColor DarkGray
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor DarkGray

# Wait for user to press Ctrl+C
try {
    while ($true) {
        Start-Sleep -Seconds 1
        # Check if any jobs have failed
        foreach ($job in $jobs) {
            if ($job.State -eq "Failed") {
                Write-Host "Job failed: $($job.Name)" -ForegroundColor Red
                Receive-Job -Job $job
            }
        }
    }
}
finally {
    Write-Host ""
    Write-Host "Stopping all services..." -ForegroundColor Yellow
    $jobs | Stop-Job -PassThru | Remove-Job
    Write-Host "All services stopped." -ForegroundColor Green
}
