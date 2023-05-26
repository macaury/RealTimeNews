/* eslint-disable no-unused-vars */
/* eslint-disable react/prop-types */
import React from "react";
import Row from "react-bootstrap/Row";

import styled from "styled-components";

import News from "./news.jsx";

import Img_logo from "./assets/logo_dark.svg";

function App() {
  const Header = styled.nav`
    height: 150px;
  `;

  const Logo = styled.section`
    display: block;
    margin: auto !important;
  `;

  const Layout_main = styled.section`
    max-width: 480px;
    min-width: 320px;
    border: 1px solid black;
  `;
  const Test_container = styled.section``;

  const Logo_Write = styled.section`
  
  color:#000;
  
  
  `;

  return (
    <>
      <Layout_main>
        <Header>
          <Logo>
            <img src={Img_logo} alt="" />
            <Logo_Write>
              <span> RealTimeNews</span>
            </Logo_Write>
          </Logo>
        </Header>
        <Row>
          <News />
        </Row>
      </Layout_main>
    </>
  );
}

export default App;
