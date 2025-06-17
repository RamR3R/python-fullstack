import React, { useEffect, useState } from 'react';
import '../styles/ms.css'

const MovieSearch = () => {

    const [movieList , setMovieList] = useState([]);
    const [searchKey , setSearchKey] = useState("");
    
    const [loading  , setLoading] = useState(false);
    const [informationText , setInformationText] = useState("");


    const fetchData = async (query) => {
        setLoading(true);
        if(query !== "")
        {
            let searchParam = query.replace(" " , "");
            const response = await fetch(`https://www.omdbapi.com/?apikey=f2359cf4&type=movie&s=${searchParam}`)
                        .then( res => res.json() )
                        .then( data => data)
                        .catch(err => console.log(err));
            console.log(response.Search);
            setMovieList(response.Search);
        }
        else
        {
            setMovieList([]);
            setInformationText("Please Enter something to find movies");
        }
        setLoading(false);
    }

    const handleSubmit = (event) =>{
        event.preventDefault();
        fetchData(searchKey);
    }

    useEffect(() => {
        fetchData(searchKey);
    },[searchKey])


  return (
    <div>
        <div className='container-main' style={{border : "none"}}>
            <h1>Moive Search App</h1>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    placeholder="Search for movies..."
                    value={searchKey}
                    onChange={(e) => setSearchKey(e.target.value)}
                    style={{
                        padding: "10px",
                        fontSize: "16px",
                        width: "300px",
                        marginTop: "10px"
                    }}
                />
                <button
                    type="submit"
                    style={{
                        padding: "10px 20px",
                        marginLeft: "10px",
                        fontSize: "16px"
                    }}
                >
                    Search
                </button>
            </form>
        </div>
        <div className='container-main'>
            {
                !searchKey.length ?
                <h5>{informationText}</h5>
                :
                <div className='movie-container'>
                    {movieList?.length &&
                        movieList.map((item , index)=>{
                            return (
                            <div 
                                style={{
                                    width : "30%",
                                    padding : "10px",
                                    border : "1px solid white",
                                    position : "relative",
                                    transition: "transform 0.8s",
                                    transformStyle: "preserve-3d"
                                }}
                                key={index}
                            >
                                <img src={item.Poster} alt="Poster" className='image' />
                                <h4>{item.Title}</h4>
                            </div>)
                        })
                    }
                </div>
            }
        </div>
    </div>
  )
}

export default MovieSearch