import React from 'react' 

export const SearchBar = () => {
    const [search, setSearch] = React.useState<string>('')

    let data: any = []

    const handleSubmit = () => {
      data.push(search)
      console.log(data)
    }

  //POST
  // async function post_query(search: string) {
  //      await fetch('http://localhost:5000/api/search_query', {
  //           method: 'POST', 
  //           mode: 'cors', 
  //           credentials: 'same-origin', 
  //           headers: {
  //             'Content-Type': 'application/json', 
  //             'Accept': 'appliction/json'
  //           },
  //           body: JSON.stringify({'query': search})
  //         }).then(response => response.json())
  //         .then(data => console.log(data))
  // }

  //PATCH
//   async function patch_query(search: string) {
//     await fetch('http://localhost:5000/api/search_query', {
//          method: 'PATCH', 
//          mode: 'cors', 
//          credentials: 'same-origin', 
//          headers: {
//            'Content-Type': 'application/json', 
//            'Accept': 'appliction/json'
//          },
//          body: JSON.stringify({'query': search})
//        }).then(response => response.json())
//        .then(data => console.log(data))
// }

//   //GET
//   async function get_query() {
//     await fetch('http://localhost:5000/api/search_query').then(response => response.json())
//     .then(data => console.log(data))
//   }

    return (
            <div className='pt-8 mx-auto'>
                <input className='border-2 border-blue-400 rounded-lg mr-2' type='text' id='search' name='search' value={search} onChange={e => setSearch(e.target.value)}/>
                <button className='border-2 border-black text-white rounded-lg px-2 bg-blue-400' onClick={() => handleSubmit()}>Search</button>
            </div>
    )
}