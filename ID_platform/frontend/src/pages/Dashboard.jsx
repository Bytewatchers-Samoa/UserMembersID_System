import { useEffect, useState } from "react";
import { getCurrentUser } from "../api/users";

// export default function Dashboard() {
//   const [user, setUser] = useState(null);
//   const [loading, setLoading] = useState(true);

//   // useEffect(() => {
//   //   async function loadUser() {
//   //     try{
//   //       const data = await getCurrentUser();
//   //       setUser(data);
//   //     } catch(err){
//   //       setError("Not authenticated");
//   //     }
//   //   }
//   //   loadUser();
//   // }, []);
//   useEffect(() => {
//     getMe()
//       .then(setUser)
//       .catch(() => {
//         alert("Not authorized");
//       });
//   }, []);

//   if (loading) return <p>Loading...</p>;
//   if (error) return <p>{error}</p>;
//   if (!user) return <p>Loading...</p>;

//   // return (
//   //   <div className="page">
//   //     <h1>Dashboard</h1>
//   //     <p>Welcome, {user.display_name}</p>
//   //     <p>Email: {user.email}</p>
//   //   </div>
//   // );
//   return (
//     <div style={{ color: "white", padding: "40px" }}>
//       <h1>Dashboard</h1>
//       <p>You are logged in 🎉</p>
//     </div>
//   );
// }
export default function Dashboard() {
  return (
    <div style={{ padding: "2rem", color: "white" }}>
      <h1>Dashboard</h1>
      <p>Test: this is the dashboard and routing works</p>
    </div>
  );
}
