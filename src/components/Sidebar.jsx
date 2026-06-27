import {
NavLink
}
from "react-router-dom";


import "../styles/layout.css";


export default function Sidebar(){


const menu=[

["Dashboard","/","bi-grid"],

["Products","/products","bi-box"],

["Camera","/camera","bi-camera-video"],

["Statistics","/statistics","bi-bar-chart"],

["Reports","/reports","bi-file-earmark-text"],

["Events","/events","bi-clock-history"],

["Settings","/settings","bi-gear"],

["Health","/health","bi-heart-pulse"]

];


return (

<div className="sidebar">


<h2>
PCS
</h2>


<p className="small text-muted">
AI Product Detection
</p>


<hr/>


{

menu.map(item=>(


<NavLink

key={item[0]}

to={item[1]}

className="side-link"

>


<i className={`bi ${item[2]}`}></i>


<span>

{item[0]}

</span>


</NavLink>


))

}


<div className="sidebar-bottom">


YOLO11n Engine

<br/>

<span>
● System Online
</span>


</div>


</div>

)

}