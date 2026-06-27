import {
useEffect,
useState
}
from "react";


import api from "../api/api";


import LiveStream from "../components/LiveStream";


import "../styles/camera.css";



export default function Camera(){


const [info,setInfo]=useState(null);



useEffect(()=>{


loadInfo();


const timer=setInterval(

loadInfo,

3000

);


return ()=>clearInterval(timer);


},[]);





async function loadInfo(){


try{


const res =
await api.get("/camera/info");


setInfo(
res.data
);


}

catch(e){

console.log(e);

}


}





async function stopCamera(){


await api.post("/camera/stop");


loadInfo();


}





return (

<div>


<div className="page-title">


<h2>

Camera Monitoring

</h2>


<p>

Live YOLO detection stream

</p>


</div>




<div className="row g-4">



<div className="col-lg-8">


<LiveStream/>


</div>





<div className="col-lg-4">


<div className="camera-panel">


<h4>

Camera Status

</h4>


<h2 className="online-text">

{

info?.running

?

"ONLINE"

:

"OFFLINE"

}


</h2>




<hr/>




<p>

Product

</p>


<h5>

{
info?.product?.name ||
"N/A"

}

</h5>



<p className="mt-3">

FPS

</p>


<h3>

{
info?.fps || 0

}

</h3>



<p>

Current Count

</p>


<h3>

{
info?.count || 0

}

</h3>




<button

className="btn btn-danger mt-3"

onClick={stopCamera}

>

Stop Camera

</button>



</div>



</div>




</div>



</div>


)

}