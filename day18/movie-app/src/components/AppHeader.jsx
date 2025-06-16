import { useState } from 'react';
import '../styles/Appheader.css';

const AppHeader = () => {

    // USE STATE
    const [counter  , setCounter] = useState(0);

    // let counter = 0;
    let name = "Ram";

    const bvc = () => {
        console.log("counter = " , counter , "nextval = " , counter + 1)
        setCounter(counter + 1)
    }

  return (
        <>
        <div className='container' style={
            {
                textAlign : 'center'
            }
        }>
            <h1>Movie Search App</h1>
            <h2>Count = {counter //state
            }</h2>

        </div>
        <button onClick={bvc}>add Count</button>
        </>
  )
}

export default AppHeader