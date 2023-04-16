import React, {useState} from 'react'
import TodoForm from "./TodoForm";
import Todo from './Todo';

function TodoList() {
    const [todos, setTodos] = useState([]);

    const addTodo = todo => {
        // Serialize text, ignore empty text
        if(!todo.text || /^\s*$/.test(todo.text)){
            return
        }
        const newTodos = [todo, ...todos]

        setTodos(newTodos)

    }

    const completeTodo = id =>{
        let updatedTodos = todos.map(todo => {
            if (todo.id === id){
                todo.isComplete = !todo.isComplete
                todo.id = todo.id * 2
            }
            return todo
        });
        setTodos(updatedTodos)
    }
  return (
    <div>
        <h3 className="m-5 justify-content-center text-center"> What are we planning today?</h3>
        <TodoForm onSubmit={addTodo}/>
        <div className="justify-contents-center p-5">
            <Todo
            todos={todos}
            completeTodo={completeTodo} />
        </div>

    </div>

  )
}

export default TodoList