import logo from './logo.svg';
import './App.css';
import List from './Components/List';
import Form from './Components/Form'; 
import { useState } from 'react';
import Counter from './Components/Counter';
import TodoApp from './TodoApp';

function App() {

  // const [players , setPlayers] = useState([]);

  // setPlayers([
  //           {name : "Jaiswal", age :22}, 
  //           {name : "Virat Kohli" , age : 38},
  //           {name :  "Shubman Gill" , age : 25} , 
  //           {name : "MSD" , age : 43}
  //         ])
  
  // const handleChange = ( newPlayer )=>{
    
  //   const newPlayersList = [...players];
  //   newPlayersList.push(newPlayer);
  //   setPlayers(newPlayersList);
  //   console.log(newPlayersList);
  // }

  return (
    <div>
      {/* <List list={players} />
      <Form handleChange={handleChange}  /> */}
      {/* <Counter /> */}
      <TodoApp />
    </div>
  );
}

export default App;
