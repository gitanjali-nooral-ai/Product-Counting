import {
useEffect,
useState
}
from "react";


import "../styles/layout.css";



export default function Navbar(){


const [time,setTime]=useState(
new Date()
);



useEffect(()=>{


const timer=setInterval(()=>{

setTime(new Date());

},1000);


return ()=>clearInterval(timer);


},[]);



return (


<nav className="top-navbar">


<div>


<h4>

Customer Product Detection

</h4>


<p>

YOLO11n + ByteTrack Monitoring System

</p>


</div>




<div className="nav-status">


<span className="status online">

<i className="bi bi-circle-fill"></i>

Camera Online

</span>



<span className="status model">

<i className="bi bi-cpu"></i>

YOLO11n

</span>



<span className="time">

<i className="bi bi-clock"></i>

{

time.toLocaleTimeString()

}

</span>


</div>


</nav>


)

}