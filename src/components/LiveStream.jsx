export default function LiveStream(){

return (

<div className="live-stream">


<div className="stream-header">

<h5>

Live Camera Feed

</h5>


<span>

● LIVE

</span>


</div>



<div className="video-box">


<img

src="http://localhost:8000/camera/stream"

alt="camera stream"

/>


</div>



</div>

)

}