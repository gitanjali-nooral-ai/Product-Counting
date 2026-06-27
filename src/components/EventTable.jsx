export default function EventTable({

events=[]

}){


return (

<div className="event-box">


<h5>

Recent Detection Events

</h5>



<table className="table table-dark">


<thead>

<tr>

<th>ID</th>

<th>Product</th>

<th>Track</th>

<th>Time</th>

</tr>

</thead>



<tbody>


{

events.map(event=>(


<tr key={event.event_id}>


<td>

{event.event_id}

</td>


<td>

{event.product_name}

</td>


<td>

#{event.track_id}

</td>


<td>

{event.counted_at}

</td>


</tr>


))


}



</tbody>


</table>


</div>

)

}