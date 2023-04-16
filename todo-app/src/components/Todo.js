import React, {useState } from 'react'
import TodoForm from './TodoForm'

function Todo({todos, completeTodo, removeTodo}) {

    const [edit, setEdit] = useState({
        id: null,
        value: ''
    })

  return todos.map((todo, index) => (
    <div
        className={todo.isComplete ? 'p-2  opacity-50 border border-2' : 'bg-dark p-2'}
        key={index} >
    <div className={todo.isComplete ? 'p-2 opacity-25' == "Done" : 'bg-light p-2'} key={todo.id}>
        <div className="card-body">
            <h4 className="card-title p-1" onClick={() => completeTodo(todo.id)}>{todo.text}</h4>
            <p className="card-text btn-outline-primary btn" onClick={() => completeTodo(todo.id)}>{todo.isComplete ? "Task Completed" : "Pending"}</p>
            <p className="card-text float-end btn btn-danger" onClick={ () => removeTodo(todo.id)}>Delete</p>
        </div>
    </div>
        <div className="bi bi-user">
        </div>
    </div>
  ));
}

export default Todo