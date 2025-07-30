import React, { useState } from 'react';
import './App.css';
import TotalDeathChart from './charts/totalDeathChart';
import DetailDeath from './charts/DetailDeath';
import TreeTagChart from './charts/treeTagChart';
import ArticleDeathChart from './charts/articlesDeathChart';
import TotalEquipmentChart from './charts/totalEquipmentChart';
import TotalEquipmentDeathChart from './charts/totalEquipmentDeathChart';
import FirePower from './charts/FirePower';
import Refugees from './charts/Refugees';
import { Switch } from 'antd';
function Dashboard(){
    const [barCharSwitch, setBarCharSwitch] = useState(true);

    function switchBarChar(value){
        setBarCharSwitch(value)
    }

    return (
        <div className="site-layout-background px-0 px-lg-4 pt-0 pt-lg-4" style={{ padding: 24, minHeight: 360 }}>
            <TotalDeathChart />
            <Switch defaultChecked onChange={switchBarChar} style={{ marginTop: 35, marginBottom: 10, marginLeft:25 }} />
            { barCharSwitch && <DetailDeath type="death" /> }
            { !barCharSwitch && <DetailDeath type="injuried"/> }
            <TotalEquipmentChart/>
            <TotalEquipmentDeathChart/>
            <Refugees/>
            <FirePower/>
            <ArticleDeathChart />
            <TreeTagChart/>
        </div>
    )
}
export default Dashboard;