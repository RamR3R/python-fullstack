const Form = (props) => {



    const handleSubmit = (event) =>{
        event.preventDefault();
        const formObj = {
            name : event.target[0].value,
            age : event.target[1].value
        }
        console.log(formObj);
        props.handleChange(formObj);
        console.log("form submitted");
    };

    return(
        <form onSubmit={handleSubmit} >
            <input type="text" placeholder="Enter Name" />
            <input type="number" placeholder="Enter Age" />

            <button type="submit" >Add Item</button>
        </form>
    )
}

export default Form;