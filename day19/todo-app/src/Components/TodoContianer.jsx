import React from 'react'
import TodoItem from './TodoItem'

const TodoContianer = (props) => {

    // const pendingList = props.list.filter(()=>{
    //     return true
    // })

  return (
    <div>
        <div>
            {
                props.list.map((element , index)=>{
                    return (<TodoItem 
                                key={index} 
                                data={element} 
                                list={props.list} 
                                setList={props.setList}
                                index={index}
                            />)
                })
            }
        </div>
        <div>
            {/*done container  */}
        </div>
    </div>
  )
}

export default TodoContianer