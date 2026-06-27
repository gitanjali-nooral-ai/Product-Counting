import {
useEffect,
useState
}
from "react";


import api from "../api/api";



export default function Health(){


const [health,setHealth]=useState(null);



useEffect(()=>{


api.get("/health/")

.then(res=>{

setHealth(res.data);

});


},[]);




if(!health)

return <h3>Checking system...</h3>;




return (

<div>


<div className="page-title">

<h2>

System Health

</h2>

</div>




<div className="row g-4">


<div className="col-md-4">


<div className="card-dark p-4">


<h5>

Database

</h5>


<h3

className={
health.database
?
"text-success"
:
"text-danger"
}

>

{

health.database
?
"ONLINE"
:
"ERROR"

}

</h3>


</div>


</div>




<div className="col-md-4">


<div className="card-dark p-4">


<h5>

Model

</h5>


<h3>


{

health.model.loaded

?

"LOADED"

:

"MISSING"

}


</h3>


</div>


</div>




<div className="col-md-4">


<div className="card-dark p-4">


<h5>

Camera

</h5>


<h3>


{

health.camera.running

?

"RUNNING"

:

"STOPPED"

}


</h3>


</div>


</div>



</div>



</div>

)

}