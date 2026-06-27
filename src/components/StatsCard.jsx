export default function StatsCard({

title,

value,

icon,

color="blue",

subtitle

}){


return (

<div className="stats-card">


<div>


<p className="stats-title">

{title}

</p>


<h2>

{value}

</h2>


<span>

{subtitle}

</span>


</div>




<div

className={`stats-icon ${color}`}

>


<i className={`bi ${icon}`}></i>


</div>



</div>

)

}