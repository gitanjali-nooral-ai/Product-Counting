import {
  useEffect,
  useState
} from "react";

import api from "../api/api";

import "../styles/event.css";


export default function Events() {

  const [events, setEvents] = useState([]);


  useEffect(() => {

    loadEvents();

  }, []);



  async function loadEvents() {

    try {

      const res = await api.get(
        "/events/?limit=100"
      );


      setEvents(
        res.data.events
      );


    } catch(error) {

      console.log(error);

    }

  }



  return (

    <div>


      <div className="page-title">

        <h2>
          Detection Events
        </h2>

        <p>
          Object tracking history
        </p>

      </div>



      <div className="timeline">


        {
          events.length === 0 ? (

            <p>
              No detection events found.
            </p>

          ) : (


            events.map(event => (


              <div
                className="timeline-item"
                key={event.event_id}
              >


                <div className="dot"></div>



                <div className="event-info">


                  <h5>
                    {event.product_name}
                  </h5>



                  <p>
                    Product ID : {event.product_id}
                  </p>



                  <span>
                    {event.counted_at}
                  </span>


                </div>


              </div>


            ))


          )
        }


      </div>


    </div>

  );

}