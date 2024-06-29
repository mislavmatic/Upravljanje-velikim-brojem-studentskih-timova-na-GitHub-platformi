import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import './GetJSON.css';

function GetJSON() {
    const [data, setData] = useState(null);
    const [expandedAsistenti, setExpandedAsistenti] = useState({});
    const [expandedGrupe, setExpandedGrupe] = useState({});

    const handleGetData = () => {
        fetch('http://localhost:5000/get_data')
            .then(response => response.json())
            .then(data => setData(data))
            .catch(error => console.error('Error:', error));
    };

    // const toggleExpanded = (setExpanded, id) => {
    //     setExpanded(prevExpanded => ({ ...prevExpanded, [id]: !prevExpanded[id] }));
    // };

    // const toggleExpandedAsistenti = (id) => {
    //     setExpandedAsistenti(prevExpanded => {
    //         const newExpanded = {...prevExpanded};
    //         newExpanded[id] = !newExpanded[id];
    //         return newExpanded;
    //     });
    // };

    // const toggleExpandedAsistenti = (id) => {
    //     setExpandedAsistenti(prevExpanded => {
    //         const newExpanded = {};
    //         // Zatvori sve grupe osim grupe asistenta na koji ste kliknuli
    //         Object.keys(prevExpanded).forEach(key => {
    //             newExpanded[key] = key === id ? !prevExpanded[key] : false;
    //         });
    //         newExpanded[id] = !prevExpanded[id];
    //         return newExpanded;
    //     });
    // };
    
    const toggleExpandedAsistenti = (id) => {
        setExpandedAsistenti(prevExpanded => {
            const newExpanded = { ...prevExpanded };
            const isCurrentlyExpanded = newExpanded[id];
    
            Object.keys(newExpanded).forEach(key => {
                if (key !== id) {
                    newExpanded[key] = false;
                }
            });
    
            newExpanded[id] = !isCurrentlyExpanded;
    
            return newExpanded;
        });
    };

    const toggleExpandedGrupe = (id) => {
        setExpandedGrupe(prevExpanded => {
            const newExpanded = {...prevExpanded};
            newExpanded[id] = !newExpanded[id];
            return newExpanded;
        });
    };

    return (
        <div className="container">
            <button onClick={handleGetData}>Get Data</button>
            {data && data.map((asistent, asistentIndex) => (
                <div key={asistent.name_asist} className="asistent">
                    {/* <h1 onClick={() => toggleExpanded(setExpandedAsistenti, asistentIndex)}>{asistent.name_asist}</h1> */}
                    <h1 onClick={() => toggleExpandedAsistenti(asistentIndex)}>{asistent.name_asist}</h1>
                    {expandedAsistenti[asistentIndex] && asistent.groups.map((group, groupIndex) => (
                        <div key={group.name_g} className="group">
                            {/* <h2 onClick={() => toggleExpanded(setExpandedGrupe, `${asistentIndex}-${groupIndex}`)}>{group.name_g}</h2> */}
                            <h2 onClick={() => toggleExpandedGrupe(`${asistentIndex}-${groupIndex}`)}>{group.name_g}</h2>
                            {expandedGrupe[`${asistentIndex}-${groupIndex}`] && (
                                <>
                                    <p>Demos: {group.name_demos}</p>
                                    <p>Zadatak: {group.name_zad}</p>
                                    <p>GitHub: <a href={group.github}>{group.github}</a></p>
                                    {group.students.map(student => (
                                        <p key={student.s_id} className="student">{student.name} {student.is_leader ? "(voditelj)" : ""}</p>
                                    ))}
                                </>
                            )}
                        </div>
                    ))}
                </div>
            ))}
        </div>
    );
}

// function GetJSON() {
//     const [data, setData] = useState(null);
//     const [expandedAsistentIndex, setExpandedAsistentIndex] = useState(null);

//     const handleGetData = () => {
//         fetch('http://localhost:5000/get_data')
//             .then(response => response.json())
//             .then(data => setData(data))
//             .catch(error => console.error('Error:', error));
//     };

//     const toggleExpandedAsistenti = (index) => {
//         setExpandedAsistentIndex(prevIndex => (prevIndex === index ? null : index));
//     };

//     return (
//         <div className="container">
//             <button onClick={handleGetData}>Get Data</button>
//             {data && data.map((asistent, asistentIndex) => (
//                 <div key={asistent.name_asist} className="asistent">
//                     <h1 onClick={() => toggleExpandedAsistenti(asistentIndex)}>{asistent.name_asist}</h1>
//                     {expandedAsistentIndex === asistentIndex && asistent.groups.map((group, groupIndex) => (
//                         <div key={group.name_g} className="group">
//                             <h2>{group.name_g}</h2>
//                             {/* Ostatak vašeg JSX-a za prikaz grupa */}
//                         </div>
//                     ))}
//                 </div>
//             ))}
//         </div>
//     );
// }

export default GetJSON;