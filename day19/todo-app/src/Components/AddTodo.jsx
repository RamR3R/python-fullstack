import React from 'react'

const AddTodo = (props) => {

    const handleForm = (event) =>{
        event.preventDefault();
        const newList = [...props.list];
        newList.push(
            {
                title : event.target[0].value,
                completed : false
            }
        );

        event.target[0].value = "";

        props.setList(newList);
    }

  return (
    <form onSubmit={handleForm}  >
        <input type='text' placeholder='Enter the Todo to add' />
        <button type='submit'>Add</button>
    </form>
  )
}

export default AddTodo