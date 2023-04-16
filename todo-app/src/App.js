import './App.css';
import TodoList from './components/TodoList';

function App() {
  return (
    <div className="Todo-App">
      <header className="App-header">
        <img src={process.env.PUBLIC_URL + '/logo.png'} width="100vw" className='float-start' alt="Logo"/>
            <h1 className="App-title"> Todo App</h1>
      </header>
      <TodoList />
      <div>
      </div>
    </div>
  );
}

export default App;
