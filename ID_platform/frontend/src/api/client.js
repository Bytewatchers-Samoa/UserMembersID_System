const API_URL = "http://localhost:8000";

//Automatically attach JWT and handles expired tokens
export async function apiFetch(url, options = {}) {
  const token = localStorage.getItem("token");

  // const headers = {
  //   "Content-Type": "application/json",
  //   ...(token && { Authorization: `Bearer ${token}` }),
  //   ...options.headers,
  // };

  // const response = await fetch(url, {
  //   ...options,
  //   headers,
  // });
  const res = await fetch(`${API_URL}${path}`, {
    ...options,
    headers: {
      "Content-Type": "application/json",
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
      ...options.headers,
    },
  });

  if (!response.ok) {
    if (response.status === 401) {
      localStorage.removeItem("token");
      window.location.href = "/";
    }
    throw new Error("Request failed");
  }

  return response.json();
}
