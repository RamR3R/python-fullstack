import React, { useEffect, useState } from 'react'

const   TodoItem = ({
    data,
    index = 0,
    handleStatusChange
}
) => {  

    useEffect(()=>{

    },[data])


  return (
    <div key={data.id} className={`todo-item ${!data.status ? 'pending' : 'done'}`}>
        <p><span>{`${index + 1}. `}</span>{data.title}</p>
        <button 
            style={{
                border : "none",
                padding : "10px",
                borderRadius : "20px",
            }}
            onClick={() => {handleStatusChange(data , index)}}
        >
            {`Change Status : ${data.status? `Pending` : `Done`}`}
        </button>
    </div>
  )
}

export default TodoItem