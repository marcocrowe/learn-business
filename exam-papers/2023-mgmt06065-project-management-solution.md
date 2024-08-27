# MGMT06065 – Project Management
### Summer Examinations 2023/2024

---

## Question 1

| Activity | Initial Node | Final Node | Estimated Duration |
|----------|--------------|------------|--------------------|
| A        | 1            | 2          | 10                 |
| B        | 1            | 3          | 12                 |
| C        | 2            | 4          | 8                  |
| D        | 2            | 3          | 4                  |
| E        | 3            | 4          | 6                  |
| F        | 3            | 5          | 6                  |
| G        | 4            | 6          | 10                 |
| H        | 4            | 5          | 12                 |
| I        | 5            | 6          | 8                  |
| J        | 5            | 7          | 8                  |
| K        | 6            | 7          | 8                  |
| L        | 7            | 8          | 10                 |

*Table 1.*

Table 1 shows the tasks and task dependencies for a project. You are required to:

### Question 1.A (12 marks)

Draw an AOA network diagram representing the project. Place the node numbers in circles and draw arrows from node to node, labeling each arrow with the activity letter and estimated time.  

### Answer 1.A

```mermaid
graph LR
  1((1)) -->|A=10| 2((2))
  1((1)) -->|B=12| 3((3))
  2((2)) -->|C=8| 4((4))
  2((2)) -->|D=4| 3((3))
  3((3)) -->|E=6| 4((4))
  3((3)) -->|F=6| 5((5))
  4((4)) -->|G=10| 6((6))
  4((4)) -->|H=12| 5((5))
  5((5)) -->|I=8| 6((6))
  5((5)) -->|J=8| 7((7))
  6((6)) -->|K=8| 7((7))
  7((7)) -->|L=10| 8((8))
```

![1724748102850](images/2023-mgmt06065-project-management-solution/1724748102850.png)

### Question 1.B (11 marks)

Identify and list all of the paths on the network diagram and the duration of each path.  

### Answer 1.B

1. **Path 1**: `1 -> 2 -> 4 -> 6 -> 7 -> 8`  
   Duration = `10 + 8 + 10 + 8 + 10 = 46`

2. **Path 2**: `1 -> 2 -> 3 -> 4 -> 6 -> 7 -> 8`  
   Duration = `10 + 4 + 6 + 10 + 8 + 10 = 48`

3. **Path 3**: `1 -> 2 -> 3 -> 5 -> 6 -> 7 -> 8`  
   Duration = `10 + 4 + 6 + 8 + 8 + 10 = 46`

4. **Path 4**: `1 -> 3 -> 4 -> 6 -> 7 -> 8`  
   Duration = `12 + 6 + 10 + 8 + 10 = 46`

5. **Path 5**: `1 -> 3 -> 5 -> 6 -> 7 -> 8`  
   Duration = `12 + 6 + 8 + 8 + 10 = 44`

6. **Path 6**: `1 -> 3 -> 5 -> 7 -> 8`  
   Duration = `12 + 6 + 8 + 10 = 36`

Thus, the paths and their corresponding durations are listed as shown above.

### Question 1.C (10 marks)

Identify the critical path of the project and explain the importance of the critical path.  

### Answer 1.C

**Critical Path Identification:**

To identify the critical path, we need to determine which of the paths has the longest duration. The critical path is the sequence of activities that determines the minimum time required to complete the project. Any delay in this path will delay the entire project.

From the paths and durations listed earlier:

1. **Path 1**: `1 -> 2 -> 4 -> 6 -> 7 -> 8`  
   Duration = 46

2. **Path 2**: `1 -> 2 -> 3 -> 4 -> 6 -> 7 -> 8`  
   Duration = 48

3. **Path 3**: `1 -> 3 -> 4 -> 6 -> 7 -> 8`  
   Duration = 46

4. **Path 4**: `1 -> 3 -> 5 -> 6 -> 7 -> 8`  
   Duration = 44

5. **Path 5**: `1 -> 3 -> 5 -> 7 -> 8`  
   Duration = 36

**Critical Path:** The critical path is **Path 2: `1 -> 2 -> 3 -> 4 -> 6 -> 7 -> 8`** with a duration of **48 units of time**.

**Importance of the Critical Path:**

The critical path is crucial because it determines the shortest possible duration to complete the project. The importance of the critical path includes:

1. **Project Duration**: The critical path dictates the minimum project completion time. Any delay in an activity on the critical path will directly delay the entire project.

2. **Resource Allocation**: Activities on the critical path require careful monitoring and efficient allocation of resources since any delays can impact the overall project timeline.

3. **Risk Management**: Identifying the critical path helps project managers focus on the most crucial activities. By ensuring these activities stay on schedule, the risk of project delays can be minimized.

4. **Scheduling and Control**: The critical path provides a clear picture of the essential tasks that need priority attention, allowing for better scheduling and control of the project.

By focusing on the critical path, project managers can ensure timely project completion and better manage potential risks and delays.

If say Path 5 is delayed by 2 units of time, the path duration of path 5 will be 36 + 2 = 38. This will not affect the project duration as it is not on the critical path. However, if Path 2 is delayed by 2 units of time, the path duration of path 2 will be 48 + 2 = 50. This will affect the project duration as it is on the critical path.

## Alternate Question 1

Given the following project activities and their dependencies, draw a Precedence Diagramming Method (PDM) network diagram. Place the activity nodes in boxes and draw arrows from node to node, indicating the dependencies between the activities. Label each node with the activity letter and its estimated duration.

| Activity | Preceding Activity | Estimated Duration |
|----------|--------------------|--------------------|
| A        | -                  | 10                 |
| B        | -                  | 12                 |
| C        | A                  | 8                  |
| D        | A                  | 4                  |
| E        | B, D               | 6                  |
| F        | B                  | 6                  |
| G        | C, E               | 10                 |
| H        | E                  | 12                 |
| I        | F, H               | 8                  |
| J        | F                  | 8                  |
| K        | G, I               | 8                  |
| L        | J, K               | 10                 |

*Table 2.*

### Alternate Question 1.A (12 marks)

**Draw a PDM Network Diagram**: Create a Precedence Diagramming Method (PDM) network diagram to represent the project's activities and their dependencies. Use rectangles for activity nodes and arrows to indicate the sequence.

### Alternate Answer 1.A

```mermaid
classDiagram
    class A {
        ID: 1
        Start: 8/8/2024
        Finish: 8/18/2024
        Duration: 10
        Res: ResA
    }
    class B {
        ID: 2
        Start: 8/8/2024
        Finish: 8/20/2024
        Duration: 12
        Res: ResB
    }
    class C {
        ID: 3
        Start: 8/19/2024
        Finish: 8/27/2024
        Duration: 8
        Res: ResC
    }
    class D {
        ID: 4
        Start: 8/19/2024
        Finish: 8/23/2024
        Duration: 4
        Res: ResD
    }
    class E {
        ID: 5
        Start: 8/24/2024
        Finish: 8/30/2024
        Duration: 6
        Res: ResE
    }
    class F {
        ID: 6
        Start: 8/21/2024
        Finish: 8/27/2024
        Duration: 6
        Res: ResF
    }
    class G {
        ID: 7
        Start: 8/31/2024
        Finish: 9/10/2024
        Duration: 10
        Res: ResG
    }
    class H {
        ID: 8
        Start: 8/31/2024
        Finish: 9/12/2024
        Duration: 12
        Res: ResH
    }
    class I {
        ID: 9
        Start: 9/13/2024
        Finish: 9/21/2024
        Duration: 8
        Res: ResI
    }
    class J {
        ID: 10
        Start: 8/28/2024
        Finish: 9/5/2024
        Duration: 8
        Res: ResJ
    }
    class K {
        ID: 11
        Start: 9/22/2024
        Finish: 9/30/2024
        Duration: 8
        Res: ResK
    }
    class L {
        ID: 12
        Start: 10/1/2024
        Finish: 10/11/2024
        Duration: 10
        Res: ResL
    }

    A --> C 
    A --> D 
    B --> E 
    D --> E 
    B --> F 
    C --> G 
    E --> G 
    E --> H 
    F --> I 
    H --> I 
    F --> J 
    G --> K 
    I --> K 
    J --> L 
    K --> L 
```

---

```mermaid
graph LR
    A["ID: 1<br/>Start: 8/8/2024<br/>Finish: 8/18/2024<br/>Duration: 10<br/>Res: ResA"]
    B["ID: 2<br/>Start: 8/8/2024<br/>Finish: 8/20/2024<br/>Duration: 12<br/>Res: ResB"]
    C["ID: 3<br/>Start: 8/19/2024<br/>Finish: 8/27/2024<br/>Duration: 8<br/>Res: ResC"]
    D["ID: 4<br/>Start: 8/19/2024<br/>Finish: 8/23/2024<br/>Duration: 4<br/>Res: ResD"]
    E["ID: 5<br/>Start: 8/24/2024<br/>Finish: 8/30/2024<br/>Duration: 6<br/>Res: ResE"]
    F["ID: 6<br/>Start: 8/21/2024<br/>Finish: 8/27/2024<br/>Duration: 6<br/>Res: ResF"]
    G["ID: 7<br/>Start: 8/31/2024<br/>Finish: 9/10/2024<br/>Duration: 10<br/>Res: ResG"]
    H["ID: 8<br/>Start: 8/31/2024<br/>Finish: 9/12/2024<br/>Duration: 12<br/>Res: ResH"]
    I["ID: 9<br/>Start: 9/13/2024<br/>Finish: 9/21/2024<br/>Duration: 8<br/>Res: ResI"]
    J["ID: 10<br/>Start: 8/28/2024<br/>Finish: 9/5/2024<br/>Duration: 8<br/>Res: ResJ"]
    K["ID: 11<br/>Start: 9/22/2024<br/>Finish: 9/30/2024<br/>Duration: 8<br/>Res: ResK"]
    L["ID: 12<br/>Start: 10/1/2024<br/>Finish: 10/11/2024<br/>Duration: 10<br/>Res: ResL"]

    A --> C 
    A --> D 
    B --> E 
    D --> E 
    B --> F 
    C --> G 
    E --> G 
    E --> H 
    F --> I 
    H --> I 
    F --> J 
    G --> K 
    I --> K 
    J --> L 
    K --> L 
```


### Alternate Question 1.B (11 marks)

**Identify the Critical Path**: After drawing the network diagram, identify and list the critical path(s) for the project, showing the total duration of the critical path.

### Alternate Answer 1.B

### Alternate Question 1.C (10 marks)

**Explain the Importance of the Critical Path**: Provide a brief explanation of why the critical path is significant in project management.

### Alternate Answer 1.C


## Question 2 (33 marks)

Managing the "triple constraint" (i.e., scope, cost, and time) of project management is often described as the most important job of a project manager. Discuss in detail EACH of these three constraints and explain why EACH of them is important to the overall success of the project.  

---

## Question 3

a) As a project manager, you have been contacted by an employee who is unhappy with her role within the project. As the employee is important to the success of the project, you offer her an immediate pay rise to solve the issue. Is this likely to be an effective strategy for resolving this issue? Explain your answer.  
**(12 marks)**

b) As part of your project management style, you have a tendency to be conciliatory when addressing likely conflicts within a project. Is this approach likely to be successful in the long term? Explain your answer.  
**(11 marks)**

c) You are concerned that a preponderance of meetings are having a negative effect on the productivity of your project. Provide any FOUR tips on running effective meetings.  
**(10 marks)**

**[End of Question 3]**

---

## Question 4

Recent trends affecting Information Technology Project Management include Globalisation, Outsourcing, and Virtual Teams. Discuss any TWO of these topics.  
**(Total Marks: 33)**

**[End of Question 4]**

---

**[END OF EXAM]**
