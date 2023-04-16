import React, {useState} from 'react'
import TodoForm from './TodoForm'

function Todo({todos, completeTodo}) {

    const [edit, setEdit] = useState({
        id: null,
        value: ''
    })

  return todos.map((todo, index) => (
    <div
        className={todo.isComplete ? 'p-2 theme-bg-primary text-light' : 'bg-dark p-2'}
        key={index} >
    <div className={todo.isComplete ? 'p-2 bg-dark text-white' == "Done" : 'bg-light p-2'} key={todo.id} onClick={() => completeTodo(todo.id)}>
        <div className="card-body">
            <h4 className="card-title p-1">{todo.text}</h4>
            <p className="card-text btn-outline-primary btn">{todo.isComplete ? "Task Completed" : "Pending"}</p>
            <p className={todo.isComplete ?  "d-none disabled" : "card-text float-end btn btn-danger" }>{todo.isComplete ? 'x' : "Delete"}</p>
        </div>
    </div>
        <div className="bi bi-user">
        </div>
    </div>
  ));
}

export default Todo