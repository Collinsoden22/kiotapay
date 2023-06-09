import React, {useState, useEffect, useRef } from 'react'

function TodoForm(props, initialState) {
    const [input, setInput] = useState("");

    const thisRef = useRef(null)

    useEffect(() =>{
      thisRef.current.focus()
    })

    const manageChange = e => {
      setInput(e.target.value);
  }

    const handleFormSubmit = e =>{
        e.preventDefault();

      props.onSubmit({
        id: new Date().toISOString().split(".")[0].replace(/[^\d]/gi,''),
        text: input,
        completed: false,
      }, setInput(" ")
      );
    }

  return (
    <div>
      <form className="m-5 justify-content-center text-center mt-5" onSubmit={handleFormSubmit}>
        <input
          type="text"
          placeholder="Add a task"
          value={input}
          name="text"
          className="form-control"
            onChange={manageChange}
            ref={thisRef}
          />
          <button className="btn btn-bg-primary m-1 float-end mt-2">Add</button>
        </form>

    </div>
  )
}

export default TodoForm