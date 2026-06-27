import {
useEffect,
useState
}
from "react";


import api from "../api/api";


import "../styles/event.css";



export default function Events(){


const [events,setEvents]=useState([]);



useEffect(()=>{


api.get("/events/?limit=100")

.then(res=>{

setEvents(res.data.events);

});


},[]);




return (

<div>


<div className="page-title">


<h2>

Detection Events

</h2>


<p>

Object tracking history

</p>


</div>




<div className="timeline">


{

events.map(event=>(


<div className="timeline-item"

key={event.event_id}>


<div className="dot"></div>


<div>


<h5>

{event.product_name}

</h5>


<p>

Track ID :

{event.track_id}

</p>


<span>

{event.counted_at}

</span>


</div>


</div>


))


}


</div>


</div>


)

}