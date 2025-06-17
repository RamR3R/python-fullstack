import React, { useEffect, useState } from 'react'
import TodoContianer from './Components/TodoContianer'
import AddTodo from './Components/AddTodo'

const TodoApp = () => {

    const [todoList , setTodoList] = useState([]);


    const fetchData = async () =>{
        const response = await fetch(`https://684e85b9f0c9c9848d285ba2.mockapi.io/todo`)
                        .then( res => res.json())
                        .then( data => data)
                        .catch( error => console.log(error))
        console.log(response);
        setTodoList(response);
    };

    useEffect(()=>{
        fetchData();
    }, [])

  return (
    <div>
        <TodoContianer list={todoList} setList={setTodoList} />
        <AddTodo list={todoList} setList={setTodoList} />
    </div>
  )
}

export default TodoApp;

