export default function LiveStream(){


return (

<div className="live-stream">



<div className="stream-header">


<div>


<h4>

Live Detection Feed

</h4>


<p>

AI product detection stream

</p>


</div>



<div className="stream-status">


<span className="pulse"></span>

LIVE


</div>


</div>





<div className="video-container">


<img

src="http://localhost:8000/camera/stream"

alt="Live camera stream"

/>



<div className="video-overlay">


<div className="recording">


<span></span>

Recording


</div>


</div>



</div>



</div>

)

}