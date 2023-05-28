//import React from "react";
import Row from "react-bootstrap/Row";


import { useState, useEffect, useRef } from "react";

import styled from "styled-components";

function News() {
  const Retangulo = styled.section`
    border-radius: 5px;
    max-width: 360px;
    height: 150px;

    background: #ffffff;
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);

    display: flex;
    justify-content: space-between;
    align-items: center;
    margin: 20px auto;
  `;

  const Img = styled.section`
    height: 79.76px;
    min-width: 100px;
    border-radius: 5px;
    border: 0.5px solid green;
    margin: 0 10px;
  `;

  const Titulo = styled.section`
    color: #8a0909;
    font-size: 18px;
    margin: 0 10px;
  `;

  const [data, setData] = useState([]);
  const carousel = useRef();

  //const proxyUrl = "https://cors-anywhere.herokuapp.com/";
  const url =
"../public/data_json/noticias.json";
  const apiUrl =  url;

  useEffect(() => {
    fetch(apiUrl)
      .then(response => response.json())
      .then(setData);
  }, [apiUrl]);


  /*
  const handleLeftClick = (e) => {
    e.preventDefault();

    carousel.current.scrollLeft -= carousel.current.offsetWidth;
  };
  const handleRightClick = (e) => {
    e.preventDefault();

    carousel.current.scrollLeft += carousel.current.offsetWidth;
  };
  
  
  <Row className="carousel" ref={carousel}> 
          {data.map(item => {
            const { image, link, titulo,id } = item;
            return (
              <Retangulo key={id} href={link}>
              <Titulo> <span>{titulo}</span> </Titulo>
              <Img>
              <img src={image} alt="" />
              </Img>
         
        </Retangulo>
            )
          })}
      </Row>
  
  

  */

  return (
    <>
      <Row>
        <Retangulo>
          <Titulo> </Titulo>
          <Img></Img>
        </Retangulo>
      </Row>
    </>
  );
}

export default News;
