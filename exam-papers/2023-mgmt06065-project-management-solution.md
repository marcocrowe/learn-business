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

All Paths.

1. 1 -> 2 -> 4 -> 5 -> 7 -> 8
1. 1 -> 2 -> 3 -> 4 -> 6 -> 7 -> 8
1. 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8
1. 1 -> 2 -> 3 -> 4 -> 5 -> 7 -> 8
1. 1 -> 2 -> 3 -> 5 -> 6 -> 7 -> 8
1. 1 -> 2 -> 3 -> 5 -> 7 -> 8
1. 1 -> 3 -> 4 -> 6 -> 7 -> 8
1. 1 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8
1. 1 -> 3 -> 4 -> 5 -> 7 -> 8
1. 1 -> 3 -> 5 -> 6 -> 7 -> 8
1. 1 -> 3 -> 5 -> 7 -> 8


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

Given the following project activities and their dependencies, draw a Precedence Diagramming Method (PDM) network diagram. Place the activity nodes in boxes and draw arrows from node to node, indicating the dependencies between the activities. Represent each activity the given fields and indicate dependencies between activities them.

| ID | Activity | Preceding Activity | Start     | Finish     | Duration | Resources |
|----|----------|--------------------|-----------|------------|----------|-----------|
| 1  | A        | -                  | 8/8/2024  | 8/18/2024  | 10       | ResA      |
| 2  | B        | -                  | 8/8/2024  | 8/20/2024  | 12       | ResB      |
| 3  | C        | A                  | 8/19/2024 | 8/27/2024  | 8        | ResC      |
| 4  | D        | A                  | 8/19/2024 | 8/23/2024  | 4        | ResD      |
| 5  | E        | B, D               | 8/24/2024 | 8/30/2024  | 6        | ResE      |
| 6  | F        | B                  | 8/21/2024 | 8/27/2024  | 6        | ResF      |
| 7  | G        | C, E               | 8/31/2024 | 9/10/2024  | 10       | ResG      |
| 8  | H        | E                  | 8/31/2024 | 9/12/2024  | 12       | ResH      |
| 9  | I        | F, H               | 9/13/2024 | 9/21/2024  | 8        | ResI      |
| 10 | J        | F                  | 8/28/2024 | 9/5/2024   | 8        | ResJ      |
| 11 | K        | G, I               | 9/22/2024 | 9/30/2024  | 8        | ResK      |
| 12 | L        | J, K               | 10/1/2024 | 10/11/2024 | 10       | ResL      |

*Table 2.*

*Table 2.*

### Alternate Question 1.A (12 marks)

**Draw a PDM Network Diagram**: Create a Precedence Diagramming Method (PDM) network diagram to represent the project's activities and their dependencies. Use rectangles for activity nodes and arrows to indicate the sequence.

### Alternate Answer 1.A

```mermaid
graph LR
    A["<b>A</b><br/>Start: 08/08/2024&nbsp;&nbsp;&nbsp;&nbsp;ID: 1 <br/>Finish: 08/18/2024&nbsp;&nbsp;&nbsp;Duration: 10<br/>Res: ResA"]
    B["<b>B</b><br/>Start: 08/08/2024&nbsp;&nbsp;&nbsp;&nbsp;ID: 2 <br/>Finish: 08/20/2024&nbsp;&nbsp;&nbsp;Duration: 12<br/>Res: ResB"]
    C["<b>C</b><br/>Start: 08/19/2024&nbsp;&nbsp;&nbsp;&nbsp;ID: 3 <br/>Finish: 08/27/2024&nbsp;&nbsp;&nbsp;Duration: 8<br/> Res: ResC"]
    D["<b>D</b><br/>Start: 08/19/2024&nbsp;&nbsp;&nbsp;&nbsp;ID: 4 <br/>Finish: 08/23/2024&nbsp;&nbsp;&nbsp;Duration: 4<br/> Res: ResD"]
    E["<b>E</b><br/>Start: 08/24/2024&nbsp;&nbsp;&nbsp;&nbsp;ID: 5 <br/>Finish: 08/30/2024&nbsp;&nbsp;&nbsp;Duration: 6<br/> Res: ResE"]
    F["<b>F</b><br/>Start: 08/21/2024&nbsp;&nbsp;&nbsp;&nbsp;ID: 6 <br/>Finish: 08/27/2024&nbsp;&nbsp;&nbsp;Duration: 6<br/> Res: ResF"]
    G["<b>G</b><br/>Start: 08/31/2024&nbsp;&nbsp;&nbsp;&nbsp;ID: 7 <br/>Finish: 09/10/2024&nbsp;&nbsp;&nbsp;Duration: 10<br/>Res: ResG"]
    H["<b>H</b><br/>Start: 08/31/2024&nbsp;&nbsp;&nbsp;&nbsp;ID: 8 <br/>Finish: 09/12/2024&nbsp;&nbsp;&nbsp;Duration: 12<br/>Res: ResH"]
    I["<b>I</b><br/>Start: 09/13/2024&nbsp;&nbsp;&nbsp;&nbsp;ID: 9 <br/>Finish: 09/21/2024&nbsp;&nbsp;&nbsp;Duration: 8<br/> Res: ResI"]
    J["<b>J</b><br/>Start: 08/28/2024&nbsp;&nbsp;&nbsp;&nbsp;ID: 10<br/>Finish: 09/05/2024&nbsp;&nbsp;&nbsp;Duration: 8<br/> Res: ResJ"]
    K["<b>K</b><br/>Start: 09/22/2024&nbsp;&nbsp;&nbsp;&nbsp;ID: 11<br/>Finish: 09/30/2024&nbsp;&nbsp;&nbsp;Duration: 8<br/ >Res: ResK"]
    L["<b>L</b><br/>Start: 10/01/2024&nbsp;&nbsp;&nbsp;&nbsp;ID: 12<br/>Finish: 10/11/2024&nbsp;&nbsp;&nbsp;Duration: 10<br/>Res: ResL"]

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

    style A text-align:left;
    style B text-align:left;
    style C text-align:left;
    style D text-align:left;
    style E text-align:left;
    style F text-align:left;
    style G text-align:left;
    style H text-align:left;
    style I text-align:left;
    style J text-align:left;
    style K text-align:left;
    style L text-align:left;
```

![alt text](image-1.png)

### Alternate Question 1.B (11 marks)

**Identify the Critical Path**: After drawing the network diagram, identify and list the critical path(s) for the project, showing the total duration of the critical path.

### Alternate Answer 1.B

**Identifying the Critical Path:**

To identify the critical path, we need to calculate the total duration of each path in the project and identify the path(s) with the longest duration, as the critical path is the one that determines the minimum time needed to complete the project.

Based on the network diagram and the dependencies, here are the possible paths:

1. **Path 1:** A -> C -> G -> K -> L
   - Duration = 10 (A) + 8 (C) + 10 (G) + 8 (K) + 10 (L) = **46 days**

2. **Path 2:** A -> D -> E -> G -> K -> L
   - Duration = 10 (A) + 4 (D) + 6 (E) + 10 (G) + 8 (K) + 10 (L) = **48 days**

3. **Path 3:** B -> E -> G -> K -> L
   - Duration = 12 (B) + 6 (E) + 10 (G) + 8 (K) + 10 (L) = **46 days**

4. **Path 4:** B -> F -> I -> K -> L
   - Duration = 12 (B) + 6 (F) + 8 (I) + 8 (K) + 10 (L) = **44 days**

5. **Path 5:** B -> F -> J -> L
   - Duration = 12 (B) + 6 (F) + 8 (J) + 10 (L) = **36 days**

6. **Path 6:** A -> D -> E -> H -> I -> K -> L
   - Duration = 10 (A) + 4 (D) + 6 (E) + 12 (H) + 8 (I) + 8 (K) + 10 (L) = **58 days**

**Critical Path:** The critical path is **Path 6: A -> D -> E -> H -> I -> K -> L** with a total duration of **58 days**.

### Alternate Question 1.C (10 marks)

**Explain the Importance of the Critical Path**: Provide a brief explanation of why the critical path is significant in project management.

### Alternate Answer 1.C

**Importance of the Critical Path:**

The critical path is a crucial concept in project management for several reasons:

1. **Project Completion Time**: The critical path determines the shortest possible time to complete the project. Knowing the critical path allows project managers to focus on the activities that cannot be delayed without affecting the overall project timeline.

2. **Resource Allocation**: By identifying the critical path, project managers can allocate resources more effectively. Activities on the critical path must be prioritized in terms of resource allocation, as any delay in these tasks directly impacts the project’s completion date.

3. **Risk Management**: Understanding the critical path helps in identifying potential risks. Since any delay on the critical path will delay the project, project managers can monitor these activities closely and develop contingency plans to mitigate risks.

4. **Project Control**: The critical path provides a clear framework for monitoring and controlling the project. Project managers can use the critical path to track progress, ensuring that the project stays on schedule.

5. **Decision Making**: In case of unforeseen circumstances or changes in project scope, understanding the critical path allows project managers to make informed decisions regarding schedule adjustments, resource reallocation, or prioritization of tasks.

In summary, the critical path is essential for ensuring that the project is completed on time, within scope, and with optimal resource usage. It serves as the backbone of effective project planning and execution.

## Question 2 (33 marks)

Managing the "triple constraint" (i.e., scope, cost, and time) of project management is often described as the most important job of a project manager. Discuss in detail EACH of these three constraints and explain why EACH of them is important to the overall success of the project.  


## Answer 2

The "triple constraint" in project management refers to the interdependent relationship between scope, cost, and time. These three constraints are critical to the success of any project, as they define the boundaries within which the project must be delivered.

**Scope:** The scope of a project encompasses all the work that needs to be completed to deliver a product, service, or result with the specified features and functions. Scope is crucial because it determines what the project will and will not include. Proper scope management ensures that the project stays aligned with the goals and expectations of stakeholders. If the scope is not well-defined or controlled, it can lead to scope creep, where additional tasks are added without corresponding adjustments to time and cost, potentially leading to project failure.

**Cost:** Cost refers to the budget allocated for completing the project. It includes all resources required, such as labor, materials, equipment, and overheads. Managing costs effectively is essential because it directly impacts the financial viability of the project. Exceeding the budget can lead to financial losses, project delays, or even the cancellation of the project. Proper cost management involves estimating costs accurately, monitoring expenditures, and controlling changes to the budget to ensure the project is completed within its financial constraints.

**Time:** Time management in a project involves creating a schedule that outlines the timeline for completing each project activity. Time is a critical constraint because delays in project timelines can have a cascading effect on other project aspects, such as increasing costs or compromising scope due to rushed work. Effective time management ensures that the project is completed on schedule, meeting deadlines that may be tied to market conditions, stakeholder expectations, or other external factors.

Each of these constraints is interrelated; a change in one constraint will likely impact the others. For example, expanding the project scope may require additional time and budget, while reducing the time allocated may necessitate a reduction in scope or an increase in costs. Therefore, balancing these three constraints is vital for project success, as it ensures that the project is delivered on time, within budget, and meets the intended objectives.


---

## Question 3

### Question 3.A **(12 marks)**

As a project manager, you have been contacted by an employee who is unhappy with her role within the project. As the employee is important to the success of the project, you offer her an immediate pay rise to solve the issue. Is this likely to be an effective strategy for resolving this issue? Explain your answer.  

### Answer 3.A

Offering an immediate pay rise to resolve an employee’s dissatisfaction with her role is not likely to be an effective long-term strategy. While a pay increase might provide temporary satisfaction and a short-term solution, it does not address the underlying issue of job dissatisfaction, which could be related to factors such as lack of role clarity, insufficient opportunities for growth, poor work-life balance, or conflicts within the team. Without addressing these root causes, the employee’s dissatisfaction may resurface, potentially leading to further disengagement or turnover. Additionally, relying on financial incentives alone can set a precedent where employees may expect pay raises as a solution to non-financial issues, which is not sustainable for the project's budget and overall team morale.

### Question 3.B **(11 marks)**

As part of your project management style, you have a tendency to be conciliatory when addressing likely conflicts within a project. Is this approach likely to be successful in the long term? Explain your answer.  

### Answer 3.B

A conciliatory approach to addressing conflicts within a project can be effective in maintaining harmony and preventing escalation of disputes in the short term. However, this approach might not be successful in the long term. If used exclusively, it can lead to unresolved issues, as it might involve compromising too much on critical project aspects or avoiding difficult but necessary conversations. Over time, this could result in unmet project objectives, reduced team performance, and a lack of respect for leadership if team members perceive the project manager as being indecisive or unwilling to enforce necessary changes. While being conciliatory can be part of a balanced conflict management strategy, it should be complemented with assertiveness and a willingness to make tough decisions when required.

### Question 3.C **(10 marks)**

To run effective meetings and prevent them from negatively impacting productivity, consider the following four tips:

### Answer 3.C

1. **Set Clear Objectives:** Ensure that each meeting has a specific purpose and clear objectives. This helps keep the meeting focused and ensures that only relevant topics are discussed.

2. **Limit Attendees:** Invite only those who are essential to the meeting’s objectives. This reduces unnecessary input and keeps the meeting efficient.

3. **Time Management:** Start and end meetings on time. Allocate time slots for each agenda item to ensure discussions do not overrun and that all necessary topics are covered.

4. **Action-Oriented Agenda:** Create an agenda that is focused on decisions and actions. This ensures that the meeting results in tangible outcomes and next steps, rather than just discussions.

Implementing these tips can help reduce the frequency and duration of meetings, thereby improving overall project productivity.

c) You are concerned that a preponderance of meetings are having a negative effect on the productivity of your project. Provide any FOUR tips on running effective meetings.  
**(10 marks)**

**[End of Question 3]**

---

## Question 4

Recent trends affecting Information Technology Project Management include Globalisation, Outsourcing, and Virtual Teams. Discuss any TWO of these topics.  
**(Total Marks: 33)**

## Answer 4

**Globalisation:**

Globalisation has significantly impacted Information Technology (IT) Project Management by increasing the scope and complexity of projects. With globalisation, projects often span multiple countries and continents, involving teams from diverse cultural backgrounds, operating in different time zones, and adhering to various regulatory environments. This geographical and cultural diversity presents both opportunities and challenges for IT project managers.

One of the key opportunities presented by globalisation is the ability to leverage a global talent pool. Organisations can access specialized skills and expertise from anywhere in the world, which can enhance the quality and innovation of IT projects. Additionally, globalisation can enable round-the-clock work, where teams in different time zones can continue progress on a project around the clock, potentially speeding up project timelines.

However, globalisation also introduces several challenges. Communication can be more complex, requiring careful management to overcome language barriers, cultural differences, and time zone discrepancies. These factors can lead to misunderstandings, delays, and conflicts if not effectively managed. Moreover, managing a distributed team requires robust tools and processes to ensure that all team members are aligned, informed, and engaged, despite the physical distance.

Effective project management in a globalised environment necessitates an understanding of cultural sensitivities, strong communication skills, and the ability to coordinate and integrate efforts across diverse teams. Project managers must also be adept at navigating international regulations, varying market conditions, and potential logistical challenges that arise from working across borders.

**Virtual Teams:**

The rise of virtual teams has become a significant trend in IT Project Management, driven by advances in technology and the increasing need for flexible working arrangements. Virtual teams consist of members who are geographically dispersed and who primarily communicate and collaborate through digital means rather than face-to-face interactions.

Virtual teams offer several advantages, such as access to a wider talent pool, cost savings on office space and travel, and increased flexibility for team members. For IT projects, which often require specialized skills that may not be available locally, virtual teams allow organisations to tap into global expertise. Additionally, virtual teams can provide a better work-life balance for employees, as they can work from locations that suit them best, leading to increased job satisfaction and potentially higher productivity.

However, managing virtual teams also comes with its own set of challenges. Communication can be more difficult in a virtual environment, as team members may lack the non-verbal cues that are present in face-to-face interactions. This can lead to miscommunications and a sense of isolation among team members. To address this, project managers need to establish clear communication protocols, use collaboration tools effectively, and foster a strong team culture despite the physical separation.

Building trust and ensuring accountability in a virtual team can also be challenging. Without the ability to observe team members directly, project managers must rely on regular check-ins, progress reports, and performance metrics to ensure that everyone is contributing effectively to the project. It is also crucial to create opportunities for virtual team members to bond and develop a sense of camaraderie, which can be achieved through virtual team-building activities and social interactions.

Overall, while virtual teams offer significant benefits for IT project management, they require careful planning and management to overcome the inherent challenges and to ensure that projects are completed successfully.

**[End of Question 4]**

---

**[END OF EXAM]**
