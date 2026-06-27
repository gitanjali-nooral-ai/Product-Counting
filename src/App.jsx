import {
Routes,
Route
}
from "react-router-dom";


import MainLayout from "./layouts/MainLayout";


import Dashboard from "./pages/Dashboard";
import Products from "./pages/Product";
import Camera from "./pages/Camera";
import Statistics from "./pages/Statistic";
import Reports from "./pages/Report";
import Events from "./pages/Event";
import Settings from "./pages/Setting";
import Health from "./pages/Health";



export default function App(){


return (

<MainLayout>


<Routes>


<Route
path="/"
element={<Dashboard/>}
/>


<Route
path="/products"
element={<Products/>}
/>


<Route
path="/camera"
element={<Camera/>}
/>


<Route
path="/statistics"
element={<Statistics/>}
/>


<Route
path="/reports"
element={<Reports/>}
/>


<Route
path="/events"
element={<Events/>}
/>


<Route
path="/settings"
element={<Settings/>}
/>


<Route
path="/health"
element={<Health/>}
/>



</Routes>


</MainLayout>

)

}