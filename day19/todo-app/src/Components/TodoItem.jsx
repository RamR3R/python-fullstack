import React from 'react'

const TodoItem = (props) => {

    const handleToggle = ()=>{
        const newItem = {...props.data }
        newItem["completed"] = !props.data.completed;
        const newArr = [...props.list];
        newArr[props.index] = newItem;
        props.setList(newArr);
    }

    const handleDelete = () =>{
        props.list.splice(props.index , 1);
        // console.log(newArr);
        console.log("old" , props.list)
        const newArr = [...props.list]
        props.setList(newArr);
    }

  return (
    <div
        className={`${ props.data.completed ? 'done' : 'pending'}`}
    >
        <p>{props.data.title}</p>
        <button onClick={handleToggle}>{props.data.completed ? "Change to Peding" : "Change to Done"}</button>
        <button onClick={handleDelete} >Del</button>
    </div>
  )
}

export default TodoItem