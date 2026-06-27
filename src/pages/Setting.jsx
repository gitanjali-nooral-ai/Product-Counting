import {
useEffect,
useState
}
from "react";


import api from "../api/api";



export default function Settings(){


const [settings,setSettings]=useState(null);



useEffect(()=>{


api.get("/settings/")

.then(res=>{

setSettings(res.data);

});


},[]);




if(!settings)

return <h3>Loading...</h3>;



return (

<div>


<div className="page-title">

<h2>

Settings

</h2>


<p>

System configuration

</p>


</div>





<div className="card-dark p-4">


<h5>

Camera

</h5>


<pre>

{
JSON.stringify(

settings.camera,

null,

2

)

}

</pre>



<h5>

Model

</h5>


<pre>

{
JSON.stringify(

settings.model,

null,

2

)

}

</pre>



</div>



</div>

)

}