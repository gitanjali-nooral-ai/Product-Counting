import { useEffect, useState } from "react";

import api from "../api/api";

import StatsCard from "../components/StatsCard";
import LiveStream from "../components/LiveStream";
import EventTable from "../components/EventTable";

import "../styles/dashboard.css";


export default function Dashboard() {


const [data,setData] = useState(null);
const [events,setEvents] = useState([]);
const [lastUpdate,setLastUpdate] = useState(null);
const [error,setError] = useState("");




useEffect(()=>{


loadDashboard();


const interval = setInterval(()=>{

loadDashboard();

},5000);


return ()=>clearInterval(interval);


},[]);





async function loadDashboard(){


try{


const dash =
await api.get("/dashboard/");


setData(dash.data);



const event =
await api.get("/events/?limit=5");


setEvents(event.data.events);



setLastUpdate(
new Date().toLocaleTimeString()
);


setError("");


}

catch(err){

console.log(err);

setError(
"Unable to connect to server"
);

}


}






if(!data)

return (

<div className="dashboard-loading">

<div className="spinner"></div>

<h4>
Loading AI Dashboard...
</h4>

</div>

);





return (

<div className="dashboard-container">


{/* HEADER */}

<div className="dashboard-header">


<div>

<h1>
AI Detection Dashboard
</h1>

<p>
Real-time product inspection monitoring
</p>

</div>



<div className="live-indicator">


<span
className={
data.camera_running
?"online"
:"offline"
}
></span>


{
data.camera_running
?
"Camera Online"
:
"Camera Offline"
}



</div>


</div>





{
error &&

<div className="alert alert-danger">

{error}

</div>

}






{/* STAT CARDS */}


<div className="row g-4">


<div className="col-xl-3 col-md-6">


<StatsCard

title="Camera Status"

value={
data.camera_running
?"ONLINE"
:"OFFLINE"
}

icon="bi-camera-video"

color={
data.camera_running
?"green"
:"red"
}

/>


</div>





<div className="col-xl-3 col-md-6">


<StatsCard

title="Current Count"

value={
data.current_count
}

icon="bi-box-seam"

color="blue"

/>


</div>





<div className="col-xl-3 col-md-6">


<StatsCard

title="Processing FPS"

value={
`${data.fps} FPS`
}

icon="bi-speedometer2"

color="orange"

/>


</div>





<div className="col-xl-3 col-md-6">


<StatsCard

title="Today's Production"

value={
data.statistics.today
}

icon="bi-calendar-check"

color="purple"

/>


</div>





</div>









{/* MAIN AREA */}


<div className="row mt-4 g-4">





<div className="col-lg-8">


<div className="dashboard-card">


<div className="card-header">


<h4>
Live Detection
</h4>


<div className="fps-badge">

{data.fps} FPS

</div>


</div>



<LiveStream/>


</div>


</div>









<div className="col-lg-4">


<div className="dashboard-card product-card">


<h4>
Active Product
</h4>



<div className="product-icon">

📦

</div>



<h2>

{
data.product.name ||
"No Product"
}

</h2>



<p>

Product ID:

<b>
{
data.product.id || "-"
}
</b>

</p>




<hr/>




<div className="product-stat">


<span>
Total Production
</span>


<strong>

{
data.statistics.total
}

</strong>


</div>




</div>



</div>




</div>









{/* EVENTS */}



<div className="dashboard-card mt-4">


<div className="card-header">


<h4>
Recent Detections
</h4>



<small>

Updated:

{lastUpdate}

</small>


</div>



<EventTable

events={events}

/>



</div>




</div>

);


}