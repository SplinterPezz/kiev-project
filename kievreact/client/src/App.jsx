import React, { useState } from 'react';
import './App.css';
import { Layout, Menu } from 'antd';
import {
  DesktopOutlined,
  PieChartOutlined,
  FileOutlined
} from '@ant-design/icons';
import Dashboard from './Dashboard';
import 'bootstrap/dist/css/bootstrap-utilities.min.css';
import 'bootstrap/dist/css/bootstrap-grid.min.css';

const { Header, Content, Footer, Sider } = Layout;

const DASHBOARD = 1
const DEATHS_PAGE = 2
const VEHICLES_PAGE = 3
const REFUGEES_PAGE = 4
const ARTICLES_PAGE = 5
const FIREPOWER_PAGE = 6
function App() {
  const [collapsed, setCollapsed] = useState(false);
  const [activePage, setActivePage] = useState(1)

  function changeActivePage(value){
    setActivePage(parseInt(value.key))
  }

  console.log(React.version);
  return (
    <Layout style={{ minHeight: '100vh'}}>
      
      <Sider collapsible className='d-none d-lg-block' collapsed={!collapsed} onCollapse={() => setCollapsed(!collapsed)}>
        <div className="logo" />
        <Menu theme="dark" onSelect={changeActivePage} defaultSelectedKeys={['1']} mode="inline">
        <Menu.Item key="1" style={{'height':'60px','paddingTop':'10px'}} icon={<PieChartOutlined />}>
            Dashboard
          </Menu.Item>
          <Menu.Item key="2" icon={<PieChartOutlined />}>
            Deaths Related
          </Menu.Item>
          <Menu.Item key="3" icon={<DesktopOutlined />}>
            Vehicles Related
          </Menu.Item>
          <Menu.Item key="4" icon={<FileOutlined />}>
            Refugees Related
          </Menu.Item>
          <Menu.Item key="5" icon={<FileOutlined />}>
            Articles Related
          </Menu.Item>
          <Menu.Item key="6" icon={<FileOutlined />}>
            FirePower Related
          </Menu.Item>
        </Menu>
      </Sider>
      <Layout className="site-layout ">
        <Header className="site-layout-background " style={{ padding: 0 }} />
        <Content className="px-0 px-lg-3">
          {activePage === DASHBOARD && <Dashboard/>}
          {activePage === DEATHS_PAGE && <><div>coming soon ...</div></>}
          {activePage === VEHICLES_PAGE && <><div>coming soon ...</div></>}
          {activePage === REFUGEES_PAGE && <><div>coming soon ...</div></>}
          {activePage === ARTICLES_PAGE && <><div>coming soon ...</div></>}
          {activePage === FIREPOWER_PAGE && <><div>coming soon ...</div></>}
        </Content>
        <Footer style={{ textAlign: 'center' }}>WE SANGO</Footer>
      </Layout>
    </Layout>
  );
}

export default App;
