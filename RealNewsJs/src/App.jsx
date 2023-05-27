/* eslint-disable no-unused-vars */
/* eslint-disable react/prop-types */
import React from "react";
import Row from "react-bootstrap/Row";

import styled from "styled-components";

import News from "./news.jsx";

import Img_logo from "./assets/logo_write.svg";

function App() {
  const Header = styled.nav`
    margin:0;
    padding:0;
    height: 80px;
    width:100%
    background: #ffffff;
    box-shadow: 2px 2px 30px rgba(0, 0, 0, 0.1);
    display:fixed;
  `;

  const Logo = styled.section`
    display: block;
    margin: 40px auto;
  `;

  const Destaque = styled.section`
    text-align: start;
    background-color: #fff;
    color: #000;
    heigth: 82px;
    font-size: 25px;
    margin: 50px 0 20px 5px;
  `;

  const Layout_main = styled.section`
    max-width: 480px;
    min-width: 320px;
  `;
  const Test_container = styled.section``;

  return (
    <>
      <Layout_main>
        <Header>
          <Logo>
            <img src={Img_logo} alt="" width={'120px'}/>
          </Logo>
        </Header>
        <Row>
          <Destaque>Destaques dos jornais</Destaque>

          <News />
        </Row>
      </Layout_main>
    </>
  );
}

export default App;
