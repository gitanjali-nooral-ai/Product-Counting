export default function CameraCard({

camera

}){


return (

<div className="camera-card">



<div className="camera-card-header">


<div>


<h5>

{camera.name}

</h5>


<p>

{camera.type?.toUpperCase()}

</p>


</div>




<div

className={

camera.online

?

"status-online"

:

"status-offline"

}

>


<span></span>


{

camera.online

?

"ONLINE"

:

"OFFLINE"

}


</div>


</div>






<div className="camera-source">


<label>

Source

</label>


<p>

{camera.source}

</p>


</div>








<div className="camera-metrics">



<div className="metric-box">


<label>

FPS

</label>


<strong>

{

camera.fps || 0

}

</strong>


</div>






<div className="metric-box">


<label>

Objects

</label>


<strong>

{

camera.count || 0

}

</strong>


</div>





<div className="metric-box">


<label>

Resolution

</label>


<strong>

{

camera.width

}

x

{

camera.height

}

</strong>


</div>



</div>





<button

className="camera-select-btn"

>


Open Camera


</button>




</div>

)

}