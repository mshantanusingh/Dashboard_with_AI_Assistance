import { useState, useEffect } from "react";
import { fetchWidgetData } from "@/lib/mcp-client";

interface UseMCPDataOptions {
  server: string;
  tool: string;
  parameters?: Record<string, unknown>;
  refreshInterval?: number;
}

export function useMCPData<T>({ server, tool, parameters = {}, refreshInterval = 0 }: UseMCPDataOptions) {
  const [data, setData] = useState<T | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    let isMounted = true;

    async function fetchData() {
      try {
        setLoading(true);
        setError(null);
        const result = await fetchWidgetData<T>(server, tool, parameters);
        if (isMounted) {
          if (result) {
            setData(result);
          } else {
            setError("Failed to fetch data");
          }
        }
      } catch (err) {
        if (isMounted) {
          setError(err instanceof Error ? err.message : "Unknown error");
        }
      } finally {
        if (isMounted) {
          setLoading(false);
        }
      }
    }

    fetchData();

    if (refreshInterval > 0) {
      const intervalId = setInterval(fetchData, refreshInterval);
      return () => {
        isMounted = false;
        clearInterval(intervalId);
      };
    }

    return () => {
      isMounted = false;
    };
  }, [server, tool, JSON.stringify(parameters), refreshInterval]);

  return { data, loading, error };
}
