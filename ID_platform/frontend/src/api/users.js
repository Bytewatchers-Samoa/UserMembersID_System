import { apiFetch } from "./client";

//create dashboard API call
export function getCurrentUser() {
  return apiFetch("http://127.0.0.1:8000/users/me");
}

export const getMe = async () => {
  // const token = localStorage.getItem("access_token");

  // const response = await axios.get(`${API_URL}/users/me`, {
  //   headers: {
  //     Authorization: `Bearer ${token}`,
  //   },
  // });

  // return response.data;
  return apiFetch("/users/me");
};
