Your task is to analyze the Apache access log located at /app/access.log.

Create a file named /app/report.json containing the following JSON object:

{
"total_requests": integer,
"unique_ips": integer,
"top_path": string
}

Success Criteria

1. Read /app/access.log.
2. Count the total number of requests.
3. Count the number of unique client IP addresses.
4. Determine the most frequently requested path.
5. Write the results to /app/report.json.
