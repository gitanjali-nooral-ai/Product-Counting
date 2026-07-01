import {
    useEffect,
    useState
}
from "react";


import api from "../api/api";

import "../styles/camera.css";



export default function Camera(){


const [info,setInfo]=useState(null);

const [cameras,setCameras]=useState([]);

const [selectedCamera,setSelectedCamera]=useState(null);


const [productId,setProductId]=useState("");



const [cameraName,setCameraName]=useState("");

const [cameraType,setCameraType]=useState("rtsp");

const [cameraSource,setCameraSource]=useState("");





useEffect(()=>{


loadInfo();

loadCameras();


const timer=setInterval(

loadInfo,

3000

);


return ()=>clearInterval(timer);


},[]);








async function loadInfo(){

try{

const res=await api.get(
"/camera/info"
);


setInfo(res.data);


}

catch(e){

console.log(e);

}

}








async function loadCameras(){

try{


const res=await api.get(
"/camera"
);


setCameras(res.data);


}

catch(e){

console.log(e);

}


}









async function addCamera(){


await api.post(

"/camera",

{

name:cameraName,

type:cameraType,

source:cameraSource,

width:640,

height:480

}

);



setCameraName("");

setCameraSource("");


loadCameras();


}









async function startCamera(){


await api.post(

`/camera/start/${selectedCamera.id}/${productId}`

);



loadInfo();


}








async function stopCamera(){


await api.post(

"/camera/stop"

);


loadInfo();


}









return (

<div className="camera-page">






<div className="camera-header">


<div>


<h1>

Camera Monitoring

</h1>


<p>

Configure cameras and monitor product detection

</p>


</div>




<div

className={

info?.running

?

"status-badge online"

:

"status-badge offline"

}

>


<span></span>


{

info?.running

?

"Running"

:

"Stopped"

}


</div>


</div>









<div className="camera-grid">







{/* Camera Management */}



<div className="card-dark camera-settings">


<h3>

Add Camera

</h3>




<input

placeholder="Camera Name"

value={cameraName}

onChange={

e=>setCameraName(e.target.value)

}

/>





<select

value={cameraType}

onChange={

e=>setCameraType(e.target.value)

}

>


<option value="rtsp">

RTSP

</option>


<option value="ip">

IP Camera

</option>


<option value="usb">

USB Camera

</option>


<option value="http">

HTTP Stream

</option>


<option value="file">

Video File

</option>


</select>






<input

placeholder="Camera Source"

value={cameraSource}

onChange={

e=>setCameraSource(e.target.value)

}

/>





<button

className="btn-primary"

onClick={addCamera}

>

Add Camera

</button>




<hr/>





<h3>

Available Cameras

</h3>





<div className="camera-list">


{

cameras.map(cam=>(


<div

key={cam.id}

className={

selectedCamera?.id===cam.id

?

"camera-item selected"

:

"camera-item"

}


onClick={

()=>setSelectedCamera(cam)

}

>


<div>

<strong>

{cam.name}

</strong>


<p>

{cam.type}

</p>


</div>



</div>


))


}


</div>




</div>










{/* Live View */}



<div className="card-dark live-panel">



<div className="panel-title">


<h3>

Live Detection

</h3>


<span>

{

info?.running

?

"Streaming"

:

"Offline"

}

</span>


</div>





<div className="video-container">


<img

src="http://localhost:8000/camera/stream"

alt="camera stream"

/>


</div>








<div className="controls">


<input

placeholder="Product ID"

value={productId}

onChange={

e=>setProductId(e.target.value)

}

/>




<button

className="btn-primary"

onClick={startCamera}

>

Start

</button>




<button

className="btn-danger"

onClick={stopCamera}

>

Stop

</button>


</div>



</div>





</div>









<div className="metrics">



<div className="card-dark metric">


<label>

FPS

</label>


<h2>

{info?.fps || 0}

</h2>


</div>





<div className="card-dark metric">


<label>

Count

</label>


<h2>

{info?.count || 0}

</h2>


</div>





<div className="card-dark metric">


<label>

Camera

</label>


<h2>

{

info?.camera?.id || "-"

}

</h2>


</div>





<div className="card-dark metric">


<label>

Product

</label>


<h2>

{

info?.product?.name || "-"

}

</h2>


</div>




</div>





</div>

)

}