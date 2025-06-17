import React from 'react'

const List = (props) => {
    const list = props.list
  return (
    <div>
              {
        list.map((element , index) => {
          console.log(element)
          return <div key={index}>
                  <h1>{element.name}</h1>
                  <p>Age = {element.age}</p>
                </div>
        })
      }
    </div>
  )
}

export default List