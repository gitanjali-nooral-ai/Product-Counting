export default function CameraCard({

camera

}){


return (

<div className="camera-card">


<div className="camera-header">


<h5>

{camera.name}

</h5>


<span className="online-dot">

● Online

</span>


</div>



<p>

Source:

{camera.source}

</p>



<div className="camera-info">


<div>

FPS

<strong>

{camera.fps}

</strong>

</div>


<div>

Count

<strong>

{camera.count}

</strong>

</div>



</div>



</div>

)

}