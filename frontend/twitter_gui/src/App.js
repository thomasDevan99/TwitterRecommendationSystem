import { SearchBar } from './components/SearchBar/SearchBar.tsx'
import { Table } from './components/Table/Table.tsx'

function App() {
  return (
    <div className=''>
      <div className='flex flex-col space-y-2'>
        <SearchBar className=''/>
        <Table />
      </div>
    </div>
  );
}

export default App;