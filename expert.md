An Introduction to Dytran: Core Concepts and Capabilities

1.0 Understanding Dytran: Purpose and Application

Dytran is a three-dimensional analysis code designed for analyzing the dynamic, nonlinear behavior of solid components, structures, and fluids. Its strategic importance lies in its explicit time integration method, making it exceptionally well-suited for simulating short, transient dynamic events. These events are often characterized by large deformations, a high degree of material and geometric nonlinearity, and complex interactions between different physical states, such as fluids and structures.

The range of problems that can be effectively analyzed with Dytran is extensive. Typical applications demonstrate its versatility and power in solving complex engineering challenges, including:

* Air bag inflation and occupant interaction
* Sheet metal forming analysis
* Weapons design calculations, such as self-forging fragments
* Birdstrike on aerospace structures
* Hydroplaning
* Response of structures to explosive and blast loading
* High-velocity penetration
* Ship collision

A key differentiator of Dytran is its dual-solver approach, which incorporates both Lagrangian and Eulerian solvers. The Lagrangian solver is ideal for modeling structures, while the Eulerian solver excels at modeling fluids. The ability to couple these solvers is critical for analyzing complex fluid-structure interactions, where materials in different states exert forces upon one another. This allows for realistic simulation of events like an underwater explosion impacting a ship's hull or the impact of a bird on an aircraft wing.

Dytran's explicit solution method is particularly advantageous for specific classes of problems where traditional implicit methods may be less efficient or struggle to converge. Explicit solutions excel in analyses that involve:

* High Material Nonlinearity: A high degree of material nonlinearity may require a small time step for accuracy, making explicit methods more efficient.
* Large Geometric Nonlinearity: Scenarios involving contact and friction can introduce potential instabilities, where a small time step is needed for both accuracy and stability.
* Stress Wave Effects: Problems where the physics demand a small time step, such as the propagation of stress waves through a material, are naturally suited for explicit analysis.
* Combined Nonlinearities: The combination of material and geometric nonlinearity with large displacements makes convergence difficult for implicit methods, giving explicit solvers a distinct advantage.

Having established the high-level purpose and applications of Dytran, the following sections will provide a more detailed examination of the specific features and concepts that enable these powerful capabilities.

2.0 A Comprehensive Overview of Dytran's Features

Dytran's power lies in a wide array of integrated features that allow for the detailed modeling of complex physical phenomena, from material properties to boundary conditions. These features provide the necessary tools to construct, constrain, and analyze sophisticated models of real-world dynamic events.

Elements and Materials

The foundation of any model is its geometric and material definition. Dytran provides a comprehensive suite of elements and material models to accurately represent physical components.

* Available Element Types:
  * Euler solid elements with four, six, and eight grid points
  * Lagrange solid elements with four, six, and eight grid points
  * Shell and membrane elements with three and four grid points
  * Beam, spring, and damper elements with two grid points
  * Spotweld elements with failure
  * Seat belt elements
* Material Modeling Capabilities:
  * General Model: A flexible model for defining elastic properties, yield criterion, equation of state, spall and failure models, and explosive burn logic.
  * Constitutive Models: Specific models are available for elastic, elastoplastic, and orthotropic materials, as well as for multilayered composites and sheet metal forming applications.
  * Specialized Models: Constitutive models are also provided for foams, honeycombs, and rubbers.
  * Strain Rate Dependency: Material models that account for strain rate effects are available for shells and beams.

Contact, Coupling, and Boundaries

Modeling the physical interactions between parts is crucial for realistic simulations. Dytran offers robust features for defining contact, coupling between different domains, and rigid boundaries.

* Contact and Coupling Methods:
  * Contact between separate Lagrangian domains
  * Efficient single surface contact for modeling buckling in shell structures
  * Adaptive contact that accounts for material erosion and failure
  * Arbitrary Lagrange-Euler (ALE) coupling
  * General Euler-Lagrange coupling for fluid-structure interactions
  * Coupling with external programs
  * Contact involving rigid ellipsoids
  * Drawbead model embedded in contact
  * Specialized contact algorithm for seat belt elements
* Rigid Bodies:
  * Rigid ellipsoids (internally or externally defined)
  * Multifaceted rigid surfaces
  * MATRIG and RBE2 definitions
  * FULLRIG rigid body definition
* Tied Connections:
  * Connections to rigid ellipsoids
  * Tying two surfaces together
  * Tying grid points and surfaces together
  * Shell edge to shell surface connections
* Rigid Walls:
  * Rigid walls for constraining Lagrangian elements
  * Rigid barriers to control Eulerian material transport

Defining the Analysis Environment

A successful analysis requires the precise application of loads, constraints, and initial conditions to replicate the real-world environment.

* Loading Types:
  * Concentrated loads and moments
  * Pressure loading
  * Enforced motion
  * Eulerian flow boundaries
  * Body forces
* Constraints:
  * Single-point constraints
  * Kinematic joints (for shell/solid connections)
  * Local coordinate systems
  * Rigid body joints
  * Drawbead model in contact
* Initial Conditions:
  * Initialization of any grid-point and/or element variable
  * Pre-state initialization from a Nastran analysis
  * Initialization of contact conditions

These features provide the building blocks for a Dytran model. The next section explores the fundamental concepts that govern how these features are defined and how they work together.

3.0 Fundamental Modeling Concepts

A successful Dytran analysis depends on a solid understanding of its fundamental building blocks. A well-constructed model is built upon a clear grasp of how solvers, grid points, coordinate systems, and constraints function and interact. This section deconstructs these core concepts.

Core Solvers: Lagrangian vs. Eulerian

Dytran’s power is rooted in its two distinct solvers. In the Lagrangian solver, the grid points of the mesh are fixed to the material. As the body deforms, the grid points move with it, causing the elements to distort. This approach essentially tracks the motion of elements of constant mass. In contrast, in the Eulerian solver, the grid points are fixed in space, creating a stationary reference frame. Material flows through this fixed mesh, and the analysis calculates the transport of mass, momentum, and energy from one element to the next.

The practical implications of this distinction are significant. The Lagrangian solver is ideal for tracking the displacement, deformation, and stress of structures with a high degree of precision. It is the preferred choice for structural components where the final deformed geometry and residual stress are important. The Eulerian solver, however, excels at modeling complex material flow with extreme deformation, such as fluids or solids undergoing shock wave propagation, where a Lagrangian mesh would become too distorted to be viable.

Defining Geometry: Grid Points and Coordinate Systems

Grid points are the fundamental entities that define the geometry of an analysis model. They are defined on GRID Bulk Data entries by specifying their spatial coordinates.

Each grid point can possess up to six components of motion, known as Degrees of Freedom (DOF). These correspond to three translations and three rotations in a rectangular system. The specific DOFs active at a grid point depend on the type of elements connected to it. For example, solid elements typically only use translational DOFs, while shell and beam elements use both translational and rotational DOFs.

Models in Dytran are defined within a coordinate system framework.

* Basic Coordinate System: A default rectangular system with its origin at (0.0, 0.0, 0.0).
* Local Coordinate Systems: To simplify the definition of complex geometries, users can define local coordinate systems which can be:
  * Rectangular
  * Cylindrical
  * Spherical

Applying Constraints

Constraints are used to restrict the motion of grid points. Permanent single-point constraints can be applied directly on a GRID entry and are automatically used for all solutions. This is useful for defining fixed supports or boundary conditions.

For models where many grid points share the same constraints, the GRDSET entry provides an efficient method for specifying default values. If a constraint field on a GRID entry is left blank, the default value from the GRDSET entry is used instead. This saves considerable data entry time, especially for plane structures where all out-of-plane motion is prevented.

Understanding these concepts is the first step toward building a model. The next section outlines the practical steps involved in preparing the input file and executing the analysis.

4.0 Preparing and Executing a Dytran Analysis

This section serves as a practical guide to the operational aspects of using Dytran. A successful analysis requires not only a well-defined model but also a correctly structured input file and an efficient use of computational resources, including memory and parallel processing.

Input File Structure

The Dytran input file is a text file organized into five primary sections, each with a distinct purpose.

* File Management Section (FMS): This optional first section contains statements that define the file names to be used during the analysis.
* Executive Control Section: This section contains Executive Control statements that can be used to set high-level options for the run, such as memory allocation.
* Case Control Section: This section contains commands that define the extent of the analysis, select output requests for printing, and specify data to be stored for postprocessing.
* Bulk Data Section: This is typically the largest section of the input file and contains all the data that defines the finite element model, including its geometry, properties, loading, and constraints.
* Parameter Options: Defined via PARAM entries in the Bulk Data Section, these options are used to control various aspects of the analysis and override default behaviors.

Memory Management

On the Windows platform, Dytran utilizes a dynamic memory allocation scheme. While the memory allocation is dynamic, the total size of available core memory is fixed once the analysis begins.

* Users can explicitly set the memory size in the input file using the MEMORY-SIZE Executive Control Statement.
* If no size is defined, Dytran allocates a default small memory size.
* At the end of each analysis, the output file reports the exact memory usage in words. This information can be used to optimize the memory settings for subsequent runs of the same or similar models, ensuring efficient use of system resources.

Leveraging Parallel Processing

To reduce computation time for large and complex analyses, Dytran supports parallel processing. This allows the analysis to be distributed across multiple processors or computers.

There are two primary parallel processing configurations:

1. Shared Memory: Utilizing multiple processors within a single computer.
2. Distributed Memory: Harnessing the combined power of a cluster of computers.

For Shared Memory systems, initiating a parallel job is straightforward. On UNIX and Linux computers, the ncpus command line option is used to specify the number of processors. For example, to run a job on four CPUs, the command would be:

dytran jid = filename ncpus = 4

The theoretical speed-up from parallel processing is described by Amdahl's Law. This model shows that the achievable speed-up depends on the fraction of the code that can be run in parallel. Since some components in Dytran are not yet parallelized, the scalability and performance gain will vary depending on the specifics of the analysis.

To help users understand the efficiency of their parallel runs, Dytran can generate a Parallel Execution Report. This report provides data on how the computational work was distributed among the available processors. It can be enabled by including the PARAM,PARALLEL,INFPAR,ON entry in the input file.

With an understanding of the technical execution of an analysis, the final step is to review best practices that promote user proficiency and successful outcomes.

5.0 Getting Started and Best Practices

This final section provides practical advice for new users to ensure a successful start with Dytran. Following established best practices, particularly regarding units, and leveraging available learning resources are key to becoming proficient with the software.

Guidance for New Users

For those new to Dytran, a structured learning approach is highly recommended.

* The simplest and quickest way to learn is to attend the training courses held by Hexagon. These courses are designed to provide an in-depth understanding of how Dytran works and how to solve problems efficiently.
* For self-learners, the following reading path is suggested:
  1. Read the introductory materials for a high-level overview.
  2. Focus on the parts of the Dytran User's Guide that describe the features needed for your first problem.
  3. Review Chapter 9: Running the Analysis for a complete procedural guide.
  4. Use the Dytran Reference Manual to look up details for specific input entries while creating the model.
* It is critical to start with simple problems and gradually increase their complexity. This approach allows you to build experience and confidence in a controlled manner.

Ensuring Consistent Units

One of the most important rules in Dytran is the management of units. Dytran does not enforce a specific unit system; therefore, the user is responsible for maintaining a consistent set of units for all input data, including geometry, material properties, loads, and mass. Mixing units within a single model will lead to incorrect results.

The following table provides examples of consistent unit systems.

Quantity	SI	Imperial	mm/kg/s/K	mm/tonne/s/K	mm/kg/ms/K
Length	m	in	mm	mm	mm
Time	s	s	s	s	ms
Mass	kg	lbf-s²/in	kg	tonne	kg
Angle	radian	radian	radian	radian	radian
Force	kg-m/s²	lbf	kg-mm/s²	tonne-mm/s²	kg-mm/ms²
Density	kg/m³	lbf-s²/in⁴	kg/mm³	tonne/mm³	kg/mm³
Stress	kg/m/s²	lbf/in²	kg/mm/s²	tonne/mm/s²	kg/mm/ms²
Energy	kg-m²/s²	lbf-in	kg-mm²/s²	tonne-mm²/s²	kg-mm²/ms²
Temperature	°K	°R	°K	°K	°K
Spec. Heat Capacity	m²/s²/°K	in²/s²/°R	mm²/s²/°K	mm²/s²/°K	mm²/ms²/°K
Heat Convection	kg/s³/°K	lbf/in/s/°R	kg/s³/°K	tonne/s³/°K	kg/ms³/°K
Thermal Conductivity	kg-m/s³/°K	lbf/s/°R	kg-mm/s³/°K	tonne-mm/s³/°K	kg-mm/ms³/°K
Thermal Expansion	m/m/°K	in/in/°R	mm/mm/°K	mm/mm/°K	mm/mm/°K

The tables below provide conversion factors to help translate common engineering units into a consistent system.

Common Units to SI Units

Quantity	Common Units	to	SI Units	Multiplication Factor
Length	meter (m)	→	meter (m)	1.0
Time	second (s)	→	second (s)	1.0
Mass	kilogram (kg)	→	kilogram (kg)	1.0
Angle	degree (°)	→	radian (rad)	1.745329 x 10⁻²
Density	kg/m³	→	kg/m³	1.0
Force	Newton (N)	→	kg-m/s²	1.0
Stress	MegaPascal (MPa)	→	kg/m/s²	1.0 x 10⁶
Temperature	Celsius (°C)	→	Kelvin (°K)	°K = °C + 273.15
Spec. Heat Capacity	J/kg/°C	→	m²/s²/°K	1.0
Heat Convection	W/m²/°C	→	kg/s³/°K	1.0
Thermal Conductivity	W/m/°C	→	kg-m/s³/°K	1.0
Thermal Expansion	m/m/°C	→	m/m/°K	1.0

US Common Units to Imperial Units

Quantity	US Common Units	to	Imperial Units	Multiplication Factor
Length	inch (in)	→	inch (in)	1.0
Time	second (s)	→	second (s)	1.0
Mass (1)	pound (lb)	→	lbf-s²/in	2.590076 x 10⁻³
Mass (2)	slug (lbf-s²/ft)	→	lbf-s²/in	8.333333 x 10⁻²
Density	lb/in³	→	lbf-s²/in⁴	2.590076 x 10⁻³
Force	pound force (lbf)	→	pound force (lbf)	1.0
Stress	lbf/in²	→	lbf/in²	1.0
Temperature	Fahrenheit (°F)	→	Rankine (°R)	°R = 459.67 + °F
Spec. Heat Capacity	Btu/lb/°F	→	in²/s²/°R	3.605299 x 10⁶
Heat Convection	Btu/in²/sec/°F	→	lbf/in/s/°R	9336.0
Thermal Conductivity	Btu/in/s/°F	→	lbf/s/°R	9336.0
Thermal Expansion	in/in/°F	→	in/in/°R	1.0

If you encounter problems or need clarification on any information, remember that you can always contact your local Hexagon representative for support.

A Guide to Element Types and Modeling Techniques in Dytran

1.0 Fundamental Concepts of Element Definition

To build an accurate and efficient simulation model in Dytran, one must first grasp the fundamental principles of element definition. The process of defining element topology, assigning geometric properties, and specifying material behavior forms the foundation of any analysis. This initial setup dictates how the model will respond to applied forces and boundary conditions, making a clear understanding of these concepts essential for success.

Elements in Dytran are defined through a hierarchical structure of three core components:

1. Connectivity Entries: Identified by a "C" prefix (e.g., CHEXA, CQUAD4), these entries define the element's topology by specifying the grid points that form its nodes. The order in which these grid points are listed is critical, as it establishes a local coordinate system within the element, which in turn defines features like the top and bottom surfaces of a shell.
2. Property Entries: Identified by a "P" prefix (e.g., PSOLID, PSHELL), these entries are referenced by the connectivity entry. They define the element's geometric properties, such as the thickness of a shell or the cross-sectional area of a beam.
3. Material Entries: The property entry references a material entry, which defines the physical behavior and constitutive model of the material from which the element is made.

The core philosophy behind Dytran's element formulation is a strategic emphasis on computational efficiency. The software employs simple elements—such as trilinear solids and bilinear shells—that use single-point integration at the element's centroid. This design choice is deliberate. Explicit analyses, for which Dytran is optimized, often require a vast number of time steps (potentially over 100,000) to solve a problem. By ensuring that the calculations for each element at every time step are as efficient as possible, Dytran enables complex simulations to be completed in a reasonable timeframe. It has been shown that using a larger number of these simple elements yields a more cost-effective solution than using a smaller number of more complex, higher-order elements.

It is important for users familiar with Nastran to note that while Dytran may use element names that are identical to those in Nastran, their underlying formulation and behavior are different. The following sections will explore the specific categories of elements available in Dytran, from structural components to specialized connectors.

2.0 Lagrangian Structural Elements

Lagrangian elements are the cornerstone of structural analysis in Dytran. Their fundamental characteristic is that the computational mesh deforms with the material, meaning that element boundaries always coincide with the same material particles throughout the simulation. This makes them the ideal choice for modeling structural components where tracking deformation, stress, and strain within a solid body is the primary objective. This section provides a detailed breakdown of the primary structural element types available in Dytran.

2.1 Solid Elements

Dytran provides three forms of Lagrangian solid elements for modeling three-dimensional components:

* CHEXA: An eight-node hexahedron (brick) element.
* CPENTA: A six-node pentahedron (wedge) element.
* CTETRA: A four-node tetrahedron element.

When meshing a model, there are significant performance differences between these types. The CHEXA element is the most robust and computationally efficient, and it is strongly recommended for use wherever possible. The CPENTA and CTETRA elements are degenerate forms of the CHEXA and exhibit significantly reduced performance. The CTETRA element, in particular, tends to be overly stiff and can produce inaccurate results. Therefore, these elements should only be used when absolutely necessary to mesh complex geometries and should be located away from critical areas of interest in the model. The material properties for all solid elements are assigned via the PSOLID entry.

2.2 Shell Elements

For modeling thin-walled structures, Dytran offers two shell elements: the quadrilateral CQUAD4 and the triangular CTRIA3. Several formulations are available to control their behavior:

* Belytschko-Tsay: This is the most computationally efficient shell formulation and is the recommended choice for most applications.
* Key-Hoff: This formulation is more computationally expensive but provides better performance and accuracy for simulations involving very large strains (greater than 5%). It is a good practice to use Key-Hoff shells in localized areas of extreme deformation while using the more efficient Belytschko-Tsay shells elsewhere.
* Hughes-Liu: Substantially more expensive than the other two, this formulation offers an advantage only if the thickness varies within a single element.
* CO-triangle: This formulation is used for the CTRIA3 element.

Element Coordinate System

The order of grid points in the connectivity entry defines the element's local coordinate system, which determines the top (positive z) and bottom (negative z) faces. However, the axis definitions differ between formulations.

For Belytschko-Tsay and Hughes-Liu shells, the z-axis is normal to the element's surface. The x-axis is determined by the vector from the first to the second grid point (G1 to G2). The y-axis is then defined by the right-hand rule.

For Key-Hoff shells, the x-axis is defined differently: it is the line connecting the midpoints of sides G1-G4 and G2-G3. Careful attention to grid point ordering is essential for consistent and correct model setup for all shell types.

2.3 Beam Elements

Beam elements are defined using either the CBAR or CBEAM entry. Both entries define the same element type; however, the CBAR entry is simpler and is therefore recommended. The geometric properties are specified using PBAR, PBEAM, or PBEAM1 entries, although only the basic data equivalent to PBAR is used from the PBEAM card.

Orientation and Formulation

A beam's orientation and local coordinate system must be explicitly defined. This can be done in two ways:

1. By specifying a third grid point that, along with the beam's two primary nodes, defines the element's xy-plane.
2. By defining an explicit vector that lies in the element's xy-plane.

Two formulations are available for beam elements:

* Belytschko-Schwer: A computationally efficient formulation.
* Hughes-Liu: A more complex formulation.

The material behavior for beams can be defined as linear elastic (MAT1) or elastoplastic (DMATEP). When using the Belytschko-Schwer formulation with an elastoplastic material, a resultant plasticity model is employed, meaning the entire cross-section yields simultaneously. A key limitation of this model is that it does not support strain-rate-dependent yield behavior.

2.4 Rod Elements

The CROD element connects two grid points and is designed to carry only axial loads (tension and compression). Unlike beam elements, rods cannot transmit torsion or bending moments. The only required property is the element's cross-sectional area, which is specified via the PROD entry.

2.5 Membrane Elements

The CTRIA3 element can be specified as a membrane, which alters its formulation. In this mode, the element carries in-plane loads but has no bending stiffness. This makes it suitable for modeling structures like thin films or fabric where bending resistance is negligible.

However, membrane elements have two key limitations:

* They are not large strain elements, so in-plane deformations should be small.
* They can only be defined with an elastic material model.

2.6 Cohesive Elements

Cohesive elements, defined using the CIFHEX entry, are designed specifically to model the behavior of adhesives or bonded interfaces between layers of other elements. Currently, Dytran only supports hexahedral cohesive elements. The element properties and material behavior are defined using the PCOHE and MCOHE entries, respectively.

The element's formulation is based on a mid-surface located between its top and bottom faces, with behavior calculated at four Gauss integration points on this surface. At each integration point, the relative displacement between the top and bottom faces is used to calculate a traction vector based on the material's normal and tangential stiffness. These tractions are then integrated over the mid-surface to determine the forces applied to the element's nodes, simulating the adhesive's response. The element's critical time step is calculated in a manner similar to a spring, based on the element's stiffness and the nodal masses of the connected layers.

These structural elements provide the building blocks for deformable bodies, which can then be linked together or to the environment using a variety of connector-type elements.

3.0 Connector and Special-Purpose Elements

In addition to elements that model deformable structures, Dytran provides a suite of idealized components used to represent springs, dampers, and generalized connections. These connector elements are essential for accurately modeling complex mechanical systems, allowing for the definition of specific forces and constraints between different degrees of freedom without the computational expense of meshing a physical connector.

3.1 Spring Elements

Dytran offers two primary types of spring elements, CSPR and CELAS, which differ in their capabilities and connectivity.

* CSPR: This element connects two grid points and can only act on translational degrees of freedom. The spring force always acts along the line connecting the two points, updating its direction as the points move.
* CELAS: This is a more general spring element that can connect both translational and rotational degrees of freedom. Unlike CSPR, a CELAS element can be "grounded" by connecting it to only one grid point. In this case, the spring force acts in a predefined, fixed direction throughout the analysis.

The behavior of these springs is defined by their property entries, which fall into three categories:

* Linear Elastic Springs (CELAS1, CELAS2): The force is directly proportional to the displacement, defined by a constant stiffness (K). Properties are defined on PELAS or CELAS2 entries.
* Nonlinear Elastic Springs (PSPRI, PELAS1): The force-deflection relationship is nonlinear and is defined by a TABLED1 entry. This allows for complex behavior, including different loading and unloading curves to model hysteresis.
* User-Defined Springs: This option allows for the implementation of custom spring behavior through a user subroutine.

3.2 Damper Elements

Similar to springs, damper elements model forces that are dependent on velocity. Dytran includes two main types: CVISC and CDAMP. Their properties are defined using PVISC or PDAMP entries.

* CVISC: This element is for translational degrees of freedom only.
* CDAMP: This is a more general damper that can be used for both translational and rotational degrees of freedom. A CDAMP element can connect one (grounded) or two grid points, and its force always acts in a predefined direction.

Damper properties are categorized as follows:

* Linear Dampers (CDAMP1, CDAMP2): The damping force is proportional to the relative velocity, defined by a damping constant (C). For a CDAMP1 element, this constant is specified on a referenced PDAMP entry. For a CDAMP2 element, it is defined directly on the connectivity card itself.
* Nonlinear Dampers: The force-velocity characteristic is defined by a TABLED1 entry, which is referenced from a PVISC or PDAMP property card, allowing for arbitrary nonlinear behavior.
* User-Defined Dampers: Custom damper behavior can be implemented via a user subroutine.

3.3 Bush Elements

The CBUSH element is a generalized three-dimensional spring-and-damper that connects two grid points across all six degrees of freedom (three translational, three rotational). It provides a versatile method for modeling complex connections with stiffness and damping in multiple directions. If only one node is specified, the element is assumed to be grounded.

The local coordinate system of the bush element can be defined using a third node, a vector, or by aligning it with a predefined coordinate system. The element's mechanical properties are defined by one of two property cards:

* PBUSH: Defines linear behavior. Stiffness (K) and damping constant (B) values are required.
* PBUSHT: Defines nonlinear behavior. This entry can reference loading curves for nonlinear force-displacement relationships, model dependencies between displacement components, and specify element failure criteria.

Having explored the Lagrangian elements that deform with a material, the focus now shifts to an entirely different approach: Eulerian elements, where material flows through a fixed computational grid.

4.0 Eulerian Elements and Advanced Meshing

The Eulerian analysis approach provides a powerful alternative to the Lagrangian method, particularly for problems involving extreme material deformation, such as fluid dynamics, explosions, or high-velocity impacts. Its core concept is a computational mesh that remains fixed in space, through which materials are free to flow. This avoids the mesh distortion issues that can terminate a Lagrangian analysis, making it uniquely suited for fluid and gas simulations.

4.1 Introduction to Eulerian Elements

An Eulerian simulation is set up by defining a fixed grid of solid elements. These elements are then initialized as being filled with one or more materials, or they can be designated as VOID (empty). As the simulation progresses, the mass, momentum, and energy of the materials are transported between elements based on the material's velocity.

Dytran supports three types of Eulerian solid elements:

* CHEXA (eight-node hexahedron)
* CPENTA (six-node pentahedron)
* CTETRA (four-node tetrahedron)

These elements share the same connectivity definitions as their Lagrangian counterparts. However, they are distinguished by referencing a PEULER property entry instead of PSOLID. A key difference is that, unlike in a Lagrangian analysis, the performance of these three element types is comparable, so they can be used interchangeably to best fit the geometry without significant performance penalties.

4.2 Graded and Glued Meshes

For computational efficiency in Eulerian simulations, it is often desirable to use a fine mesh only in the region of primary interest and a much coarser mesh elsewhere. This technique is known as creating a graded mesh. Dytran facilitates this through a powerful gluing algorithm, activated by the PARAM,GRADED-MESH command.

When activated, the gluing algorithm performs the following steps automatically:

1. It sorts the Eulerian elements into connected groups.
2. It identifies and removes coarse elements that are completely covered by elements from a finer mesh group. The criterion for removal can be based on element volume or element number.
3. It creates special faces at the interface between the different mesh groups to ensure a seamless connection and proper transport of material properties across the boundary.

4.3 Implementation and Visualization

The PARAM,GRADED-MESH method provides a streamlined approach to creating graded meshes, replacing an older, more cumbersome technique that required defining multiple Euler domains with porous coupling surfaces.

A straightforward way to construct a graded mesh is to use MESH,BOX entries:

1. Define the coarse mesh for the entire problem domain.
2. Define a separate, finer mesh that covers the specific area of interest.
3. Ensure the fine mesh fits neatly within the boundaries of the coarse mesh.
4. Activate the gluing algorithm with PARAM,GRADED-MESH.

When visualizing the results of a graded mesh simulation in a post-processor like Patran, users may notice a lack of smoothness in fringe plots at the mesh interfaces. This visual artifact is caused by the presence of "hanging nodes"—grid points that belong to the fine mesh but not the coarse mesh. When the post-processor averages values at grid points to create a plot, these hanging nodes can cause discontinuities. This is a visualization issue only and can be avoided by post-processing using element-based values instead of node-based values.

Moving from the modeling of deformable bodies and fluids, the next section addresses the simulation of completely nondeformable rigid structures.

5.0 Modeling Rigid Structures and Masses

In many simulations, certain components are significantly stiffer than others, or their deformation is not of interest to the analysis. Dytran allows these components to be modeled as rigid structures—perfectly nondeformable bodies. This is a versatile and computationally efficient feature, as the solver does not need to compute internal stresses or strains for these parts, greatly reducing calculation time.

5.1 Rigid Ellipsoids (RELLIPS)

Dytran provides a predefined geometric shape for a rigid body: the ellipsoid. A rigid ellipsoid is defined using the RELLIPS entry, which specifies its mass, spatial orientation, shape (via the lengths of its three axes), and initial translational or rotational motion. The moments of inertia are calculated automatically assuming a uniform mass distribution.

5.2 User-Defined Rigid Bodies (RIGID)

For components with arbitrary shapes, the RIGID entry can be used to make any user-defined surface nondeformable. The RIGID entry references a SURFACE definition and specifies the body's mass, center of gravity, and inertia tensor, allowing for the creation of rigid bodies of nearly any geometry.

5.3 Rigid Element Constraints (RBE2)

The RBE2 entry is a constraint element that enforces the same displacement for specific degrees of freedom across a set of grid points. This is useful for modeling connections like pin joints or rigid planes.

The FULLRIG option on the RBE2 entry couples all six degrees of freedom, causing the connected grid points to behave as a single, unified rigid body. This is distinct from a normal RBE2, which averages the motion of the specified degrees of freedom and may not properly transmit rotation.

The use of RBE2 elements is subject to several restrictions. A grid point connected to an RBE2 cannot be:

* Subjected to enforced motion
* Attached to a rigid body
* Attached to a tied connection
* A secondary contact for a rigid wall

5.4 Rigid Materials (MATRIG)

An alternative and more efficient method for making a portion of a finite element mesh rigid is to use the MATRIG material entry. By replacing a standard material definition with MATRIG, all elements referencing it will behave as a single rigid body. This approach is more computationally efficient than using an RBE2 with the FULLRIG option because the solver can skip the material calculations for these elements entirely.

Multiple MATRIG and RBE2-FULLRIG definitions can be merged into a single, larger rigid assembly using PARAM,MATRMERG or PARAM,MATRMRG1. This allows complex rigid structures to be built from several simpler definitions.

5.5 Lumped Masses (CONM2)

The CONM2 entry allows for the application of additional mass and inertia to a specific grid point. This is useful for representing non-structural mass or for ensuring that grid points connected only to massless elements (like springs) have the necessary mass for the explicit time integration scheme.

After defining the geometry and constraints of a model, the final critical step is to select the material models that govern the physical behavior of all deformable elements.

6.0 Constitutive Models and Material Selection

The selection of an appropriate material model is one of the most critical steps in building a simulation. The accuracy of the final results is fundamentally limited by the quality of the input material data and the suitability of the chosen constitutive model to represent the material's real-world behavior. A sophisticated mesh and advanced element formulation cannot compensate for an inaccurate or inappropriate material definition.

6.1 Guiding Principles for Model Selection

Given the wide array of available material models, choosing the right one can be challenging. The following principles should guide the selection process:

* Keep it simple: Whenever possible, use the simplest material model that can capture the necessary physics. Simpler models are more computationally efficient and their behavior is easier to interpret.
* Consider data availability: The accuracy of a simulation depends directly on the accuracy of the input material properties. For dynamic, large-strain conditions, reliable data can be scarce and difficult to obtain. If high-quality data for a complex model is not available, using a simpler model may yield more reliable results.
* Perform sensitivity studies: If there is uncertainty about material properties, it is good practice to run several analyses with different models or assumptions. This helps determine how sensitive the results are to variations in the input data.

6.2 Compatibility with Dyna Materials

For historical reasons and to support legacy models, Dytran can process material definitions that originated from Dyna. The material names and formats from Dyna Version 3 can be used directly. Some of these materials are implemented natively in Dytran under the same name, while others are automatically mapped to an equivalent Dytran material model, as shown in the table below.

Dyna Version 3 Name	Material Description	Dytran Equivalent Name
MAT1	Isotropic, linear, elastic material.	(MAT1)
DYMAT1	Isotropic, elastic material.	DMATEP
DYMAT2	Orthotropic, elastic material. (Solid Lagrangian elements.)	DMATOR
DYMAT3	Elastoplastic, nonlinear material with isotropic hardening.	DMATEP
DYMAT5	Nonlinear, elastic perfectly plastic soil and crushable foam.	DYMAT14
DYMAT6	Viscoelastic material	DMAT + SHRLVE
DYMAT12	Elastoplastic, nonlinear material with isotropic hardening.	DMATEP
DYMAT12A	Like DYMAT12, but the shear and bulk modulus define the material behavior.	DMATEP
DYMAT13	Nonlinear, isotropic, elastotropic material with failure.	DMATEP
DYMAT13A	Like DYMAT13 but the shear and bulk modulus define the material behavior.	DMATEP
DYMAT14	Nonlinear, elastic perfectly plastic, compressible soil and crushable foam, with failure.	(DYMAT14)
DYMAT24	Elastoplastic, nonlinear, plastic material with isotropic hardening. Stress-strain curve is piecewise linear.	(DYMAT24)
DYMAT26	Orthotropic crushable material. (Solid Lagrangian elements.)	(DYMAT26)

6.3 Supported Material Models by Element Type

The following table provides a comprehensive reference for which material models are compatible with specific element types and lists the required bulk data entries.

Material Type	Supported Elements and Required Entries
Isotropic Elastic Material	<ul><li>Shell and membrane elements: DMATEL</li><li>Lagrangian solid elements: DMAT + EOSNA + SHREL</li><li>Eulerian solid elements: DMAT + EOSNA + SHREL</li></ul>
Isotropic Nonlinear Elastic Material	<ul><li>Lagrangian solid elements: DMAT + EOSNA + SHRPOL</li><li>Eulerian solid elements: DMAT + EOSNA + SHRPOL</li></ul>
Isotropic Fluid Material	<ul><li>Lagrangian solid elements: DMAT + EOSNA</li><li>Eulerian solid elements: DMAT + EOSNA</li></ul>
Orthotropic Elastic Material	<ul><li>Shell and membrane elements: MAT8</li><li>Lagrangian solid elements: DMATOR</li></ul>
Composite Material	<ul><li>Shell elements: MAT8</li></ul>
Composite Material with Damage	<ul><li>Shell elements: MAT8 + MAT8A</li></ul>
Anisotropic Elastic Material (Classical Laminate Theory)	<ul><li>Shell elements: MAT8, MAT2</li></ul>
Isotropic Elastoplastic Material	<ul><li>Beam elements: DMATEP + YLDVM, DYMAT24</li><li>Shell elements: DMATEP + YLDVM, DYMAT24</li><li>Lagrangian solid elements: DMAT + EOSNA + SHREL + YLDVM, DYMAT24</li><li>Eulerian solid elements: DMAT + EOSNA + SHREL + YLDVM</li></ul>
Isotropic Elastoplastic Material with Failure	<ul><li>Beam elements: DMATEP + YLDVM + FAILEX, DYMAT24</li><li>Shell elements: DMATEP + YLDVM + FAILEX, DYMAT24</li><li>Lagrangian solid elements: DMAT + EOSNA + SHREL + YLDVM + FAILEX, DYMAT24</li><li>Eulerian solid elements: DMAT + EOSNA + SHREL + YLDVM + FAILEX</li></ul>
Kinematic/Isotropic Plasticity	<ul><li>Beam elements: DMATEP + YLDVM, DYMAT24</li><li>Shell elements: DMATEP + YLDVM, DYMAT24</li><li>Lagrangian solid elements: DMAT + EOSNA + SHREL + YLDVM, DYMAT24</li><li>Eulerian solid elements: DMAT + EOSNA + SHREL + YLDVM</li></ul>
Resultant Plasticity	<ul><li>Beam elements: DMATEP</li></ul>
Rate Power Law Plasticity Model	<ul><li>Shell elements: DMATEP + YLDRPL</li><li>Lagrangian solid elements: DMAT + EOSNA + SHREL + YLDRPL</li><li>Eulerian solid elements: DMATEPYLDRPL</li></ul>
Johnson/Cook Plasticity Model	<ul><li>Shell elements: DMATEP + YLDJC</li><li>Lagrangian solid elements: DMAT + EOSNA + SHREL + YLDJC</li><li>Eulerian solid elements: DMAT + EOSNA + SHREL + YLDJC</li></ul>
Mohr-Coulomb Plasticity Model	<ul><li>Eulerian solid elements: DMAT + EOSNA + SHREL + YLDMC</li></ul>
Tanimura/Mimura Plasticity Model	<ul><li>Shell elements: DMATEP + YLDTM</li><li>Lagrangian solid elements: DMAT + EOSNA + SHREL + YLDTM</li><li>Eulerian solid elements: DMAT + EOSNA + SHREL + YLDTM</li></ul>
Zerilli/Armstrong Plasticity Model	<ul><li>Shell elements: DMATEP + YLDZA</li><li>Lagrangian solid elements: DMAT + EOSNA + SHREL + YLDZA</li><li>Eulerian solid elements: DMAT + EOSNA + SHREL + YLDZA</li></ul>
User-defined Plasticity	<ul><li>Lagrangian solid elements: DMAT + EOSNA + SHREL + YLDEX</li><li>Eulerian solid elements: DMAT + EOSNA + SHREL + YLDEX</li></ul>
Strain-rate Dependent Plasticity	<ul><li>Beam elements: DYMAT24</li><li>Shell elements: DYMAT24</li><li>Lagrangian solid elements: DYMAT24</li></ul>
Piece-wise Linear Plasticity	<ul><li>Beam elements: DMATEP + YLDVM, DYMAT24</li><li>Shell elements: DMATEP + YLDVM, DYMAT24</li><li>Lagrangian solid elements: DMAT + EOSNA + SHREL + YLDVM, DYMAT24</li><li>Eulerian solid elements: DMAT + EOSNA + SHREL + YLDVM</li></ul>
Piece-wise Linear Plasticity with Isotropic Hardening	<ul><li>Beam elements: DMATEP + YLDVM, DYMAT24</li><li>Shell elements: DMATEP + YLDVM, DYMAT24</li><li>Lagrangian solid elements: DMAT + EOSNA + SHREL + YLDVM, DYMAT24</li></ul>
Piece-wise Linear Plasticity with Isotropic Hardening and Failure	<ul><li>Beam elements: DMATEP + YLDVM + FAILEX, DYMAT24 + FAILEX</li><li>Shell elements: DMATEP + YLDVM + FAILEX, DYMAT24 + FAILEX</li><li>Lagrangian solid elements: DMAT + EOSNA + SHREL + YLDVM + FAILEX, DYMAT24 + FAILEX</li></ul>
Nonlinear Plasticity	<ul><li>Lagrangian solid elements: DMAT + EOSNA + SHRPOL + YLDPOL</li><li>Eulerian solid elements: DMAT + EOSNA + SHRPOL + YLDPOL</li></ul>
Anisotropic Plasticity Model (Sheet-metal - Krieg)	<ul><li>Shell elements: SHEETMAT, BARLT89</li></ul>
Anisotropic Plasticity Model with FLD (Sheet-metal - Krieg)	<ul><li>Shell elements: SHEETMAT, BARLT89</li></ul>
Linear Viscoelastic Material Model	<ul><li>Lagrangian solid elements: DMAT + EOSNA + SHRLVE</li></ul>
Soil And Concrete (Cap) Material Model	<ul><li>Lagrangian solid elements: DYMAT25</li></ul>
Soil and Crushable Foam	<ul><li>Lagrangian solid elements: DYMAT14</li></ul>
Soil and Crushable Foam with Failure	<ul><li>Lagrangian solid elements: DYMAT14</li></ul>
Combustible material	<ul><li>Eulerian solid elements: DMAT + EOSDEF</li></ul>
Crushable Foam (Polypropylene)	<ul><li>Lagrangian solid elements: FOAM1</li></ul>
Crushable Foam with Hysteresis and Strain Rate Dependency	<ul><li>Lagrangian solid elements: FOAM2</li></ul>
Orthotropic Crushable Material	<ul><li>Lagrangian solid elements: DYMAT26</li></ul>
Mooney-Rivlin Rubber	<ul><li>Lagrangian solid elements: RUBBER1</li></ul>
Explosive Material (JWL)	<ul><li>Eulerian solid elements: DMAT + EOSJWL</li></ul>
Ignition and Growth Explosive Material	<ul><li>Lagrangian solid elements: DMAT + EOSIG</li></ul>
Polynomial Equation of State	<ul><li>Lagrangian solid elements: DMAT + EOSNA</li><li>Eulerian solid elements: DMAT + EOSNA</li></ul>
Polynomial Equation of State with Viscosity	<ul><li>Eulerian solid elements: DMAT + EOSNA</li></ul>
Tait's Equation of State with Cavitation Model	<ul><li>Lagrangian solid elements: DMAT + EOSTAIT</li><li>Eulerian solid elements: DMAT + EOSTAIT</li></ul>
Tait's Equation of State with Cavitation and Viscosity	<ul><li>Eulerian solid elements: DMAT + EOSTAIT</li></ul>
User-defined Equation of State	<ul><li>Eulerian solid elements: DMAT + EOSEX</li></ul>
Perfect Gas	<ul><li>Lagrangian solid elements: DMAT + EOSGAM</li><li>Eulerian solid elements: DMAT + EOSGAM</li></ul>
Rigid Material	<ul><li>Beam elements: MATRIG</li><li>Shell elements: MATRIG</li><li>Lagrangian solid elements: MATRIG</li></ul>

In addition to the models listed above, a failure model based on the minimum time step can be combined with any Lagrangian solid or shell material definition. This failure model is activated using the PARAM, FAILDT entry.

Technical Reference: Advanced Loading, Constraints, and Contact Mechanics in Multi-Physics Simulation

1. Fundamental Principles of Body Forces and Gravitational Acceleration

In high-fidelity dynamic simulations, the strategic modeling of body forces is the mandated approach for resolving localized transient gradients and ensuring global physical validity. Whether operating within a Lagrangian framework—where the mesh deforms with the material—or an Eulerian framework—where material flows through a fixed mesh—the accurate application of acceleration fields is what grounds a model in a realistic physical environment. Mismanagement of these forces typically results in non-physical equilibrium or artificial instabilities that compromise the structural integrity of the entire analysis.

Global vs. Localized Body Forces Computational efficiency depends on selecting the appropriate entry for acceleration:

* Global Forces (GRAV): The GRAV entry applies a uniform acceleration vector across the entire simulation. In an Eulerian mesh, this affects all material mass present, defining a constant environmental field such as gravity.
* Localized Forces (BODYFR1): For discrete material regions or time-dependent acceleration requirements, BODYFR1 is employed. This provides the granularity needed to simulate transient events where forces vary as the simulation progresses, rather than applying a static global field.

The selection between these entries is a matter of computational strategy. While GRAV entries are optimized for constant environmental conditions, BODYFR1 entries provide the architectural control necessary for high-intensity transient loads. This distinction ensures that the bulk material behavior responds correctly to external fields without introducing numerical artifacts in material-intensive regions.

While body forces act on the bulk material mass, point-specific interactions require a distinct methodology: concentrated loads.

2. Mechanics of Concentrated Loads and Moments

Nodal excitations serve as the primary mechanism for simulating discrete external interactions. In transient analysis, where forces evolve rapidly, the integration of time-varying functions is essential for capturing the high-frequency response of the system.

Implementation of Loads and Moments Fixed-direction loads and moments are applied to grid points using specific entries driven by TLOAD1 (table-referenced) or TLOAD2 (function-defined) entries. The scale factor logic is precise: the magnitude of the vector defined in the load entry itself acts as an additional scale factor.

Entry Type	Target	Direction Definition	Scaling Logic
FORCE / FORCEn	Grid Point	Vector components (basic CS)	Scale Factor x Vector Magnitude x Curve Value
MOMENT / MOMENTn	Grid Point	Vector components (basic CS)	Scale Factor x Vector Magnitude x Curve Value
DAREA	Grid Point	Coordinate system direction	Scale Factor x Curve Value

Rigid Body Dynamics and Computational Efficiency For rigid bodies defined via MATRIG or RBE2, concentrated loads or enforced motions must be applied at the rigid body center of gravity (CG). This is architected by referencing the rigid body property ID rather than individual grid points. From a computational perspective, the RBCNT algorithm provides a significant efficiency gain: during calculation cycles, the solver only updates the translational displacement and rotational angle at the CG. It avoids the overhead of updating every dependent node on the rigid body, rotating the contact forces back to the original configuration only when necessary to resolve interactions.

Static loads often necessitate predefined initial states for the system to reach equilibrium before transient analysis begins.

3. Prescribing System State: Initial Conditions vs. Enforced Motion

A successful simulation requires a strategic distinction between the system’s starting state—its Initial Conditions—and its Enforced Motion, which represents a guided trajectory throughout the analysis.

Initializing the Model and Volume Control Initialization defines the velocity or variable states at t=0:

* Grid and Element Levels: TIC, TICGP, and TICEL assign initial values to nodes and element variables.
* Eulerian Volume Initialization: The TICEUL entry, used with PEULER1, allows for material assignment within geometric regions (spheres, cylinders, boxes). To resolve multifaceted surfaces, the MATINI entry is critical. It provides INSIDE or OUTSIDE functionality, allowing the architect to initialize material specifically within complex volumes or, conversely, initialize everything outside a defined surface as a void or secondary material.

The "Opaque Paper" Analogy The TICEUL hierarchy prevents material ambiguity. Imagine shapes cut out of opaque paper: the lowest "Level" is placed first, and each higher Level is placed on top. If an element resides in overlapping regions, it adopts the properties of the region with the highest Level number. Defining overlapping regions with identical Level numbers will trigger a solver error.

Enforced Motion Strategic Logic Unlike initial conditions, enforced motion (via TLOAD) dictates velocity throughout the analysis. Because explicit solvers require velocity inputs, displacement-based motion must be differentiated into a velocity-versus-time characteristic to be compatible.

External boundaries and flow limits must be defined to contain or facilitate these internal state changes.

4. Eulerian Boundary Dynamics and Flow Control

Managing material flux and pressure boundaries is strategically vital for simulating open systems, such as wind tunnels, or contained environments with specific internal pressures.

Boundary Control Mechanisms

* Default Barriers: Any exterior face of an Eulerian mesh without a specific boundary condition acts as a fixed barrier through which material cannot flow.
* Flow Entries: FLOW, FLOWSQ, and FLOWDIR define velocity, pressure, and density. If only pressure is specified, the entry acts as a pressure boundary.
* Cyclic and Hydrostatic Conditions: FLOWC enables cyclic boundaries where outflow from one region becomes inflow for another. PARAM, HYDSTAT is used to preset element densities and pressures to follow a hydrostatic profile, essential for underwater modeling.

Flexibility through Subroutines For non-standard boundary logic, user subroutines like FLOWEX (face-based) and FLOWXDR (direction-based) allow for complex, logic-driven flow behaviors that exceed table-based definitions.

This fluid boundary control transitions to the interaction between discrete surfaces in contact.

5. Contact Surface Mechanics and Penalty Stiffness Optimization

Contact modeling prevents interpenetration and facilitates energy transfer. The strategic "So What?" for practitioners: the secondary surface must always have a finer mesh density than the primary surface. If the primary mesh is finer, secondary nodes may "miss" primary segments, resulting in non-physical interpenetration and "hourglassing"—a zero-energy mode that causes mesh instability.

Contact Categories

1. General Contact: Models contact, separation, and sliding between distinct surfaces.
2. Single Surface: Essential for buckling; prevents a surface from penetrating itself.
3. Discrete Grid Points: Allows specific nodes to interact with a primary surface without a continuous secondary mesh.

Penalty Stiffness and Safety Factors Standard mass-based stiffness can be overestimated when element sizes differ significantly. Material-based stiffness is calculated based on the Bulk Modulus (K), Area (A), and the characteristic diagonal (d).

* Quad Elements: Stiffness = (K x A / longer diagonal) x Safety Factor.
* Tria Elements: Stiffness = (K x A / longest side) x Safety Factor.

Architectural Note on Safety Factors: The default Safety Factor depends on the activation parameter. When using PARAM,CONTACT,STIFF,SLSTIFF, the default Safety Factor is 1.0. However, when using the VERSION=STIFF option, the default Safety Factor is reduced to 0.1.

These principles extend to advanced interface interactions involving permanent bonds and friction.

6. Advanced Interface Interactions: Tied Connections and Friction

Tied connections (RCONN) are used for mesh refinement, joining disparate mesh densities without the excessive stiffness of pentagonal or tetrahedral transitions.

Tied Connection Types

* Surface-to-Surface: Joins two surfaces; the finer mesh must be the secondary surface.
* Grid-to-Surface: Ties translational degrees of freedom only.
* Shell-to-Shell: Ties shell edges to surfaces, maintaining the angle between shells by coupling rotational degrees of freedom.

Large Offsets (PENSHEL) and Failure When components are separated by a significant gap, PENSHEL uses a penalty method. The penetration (pen) is calculated as the difference between the secondary point location (accounting for the gap distance and normal vector) and the projection point on the primary surface: pen = (s_1 - p) \cdot z. Because large gaps create large moments, additional nodal rotational inertia is automatically added—calculated from translational mass and gap distance—to prevent numerical instability.

Failure and Stress Calculation: Tied contacts can fail based on normal and shear stress limits. The contact stress is calculated as the contact force divided by the product of the element area and a Weight Factor (W):

* W = 1/4 for Quad elements.
* W = 1/3 for Tria elements.

Friction Limits: In sheet metal forming, the TAUMAX option limits friction to a specific shear stress, defined as Yield / \sqrt{3}. This prevents non-physical friction forces from stalling the simulation.

7. Specialized Physics: Detonation, Deflagration, and Viscosity

Advanced simulations involving energetic events or realistic fluid behavior require specialized equations of state (EOS) and viscosity handling.

Energetic Events

* Detonation: Handled via DETSPH, which defines a spherical detonation wave moving at a specific speed through materials referencing EOSJWL.
* Deflagration: Eulerian elements referencing EOSDEF can burn if they are within a region marked by DEFMAT=1. Burning is pressure-driven; ignition is typically triggered by increasing initial specific internal energy.

Viscosity and Navier-Stokes Transition Activating viscosity transitions the simulation from Euler equations to Navier-Stokes equations, enforcing a "no-slip" condition at boundaries.

* Symmetry Plane Warning: When viscosity is active, standard wall entries cannot be used to simulate symmetry planes because they enforce a no-slip condition. To simulate a symmetry plane under viscous conditions, a flow boundary must be defined with zero normal velocity and unspecified tangential velocity.
* Solver Selection: First-order solvers introduce "artificial viscosity" that can overshadow physical viscosity and artificially thicken the boundary layer. For high Reynolds number flows, the Roe solver is the strategic choice as it minimizes artificial viscosity.
* Skin Friction: If the mesh cannot resolve the boundary layer, empirical skin friction coefficients (C_f) are used to relate shear stress to density (\rho) and relative tangential velocity (v): Shear Stress = 0.5 \cdot \rho \cdot v^2 \cdot C_f.

The synergy between loading, constraints, and contact defines the predictive power of the simulation, transforming simple structural models into complex multi-physics digital twins.

Technical Guide to Fluid-Structure Interaction: Advanced Coupling Methodologies

1. Foundations of Eulerian-Lagrangian Interaction

In the realm of high-fidelity physical simulations, Fluid-Structure Interaction (FSI) represents a primary computational bottleneck. The strategic importance of coupling Eulerian and Lagrangian meshes lies in the necessity of simulating environments where fluid flow and structural deformation are intrinsically linked. Eulerian solvers are peerless in modeling material flow through space, while Lagrangian solvers are the standard for stress analysis of solid structures. The coupling algorithm acts as the bridge, ensuring that pressure and stresses are accurately transferred across these disparate mathematical frameworks.

A fundamental concept for the simulation architect is the COVER field on the COUPLE entry. This field dictates what part of the Euler domain is rendered inaccessible to fluid. Understanding this logic is crucial:

* INSIDE: The internal volume of the Lagrangian structure is treated as a "void" where Eulerian material cannot exist. This is the standard configuration for projectiles, where the internal mass is handled by the Lagrangian solver alone.
* OUTSIDE: Eulerian material is contained within the structure, such as in an inflating air bag, meaning the region outside the surface is inaccessible to the fluid.
* NONE: Used when fluid must coexist on both sides of the structural barrier.

By defining these boundaries, the architect ensures the simulation honors the physical volume of the structure. Transitioning from this foundation, the choice of coupling methodology—ALE, Fast, or Auto—depends entirely on the complexity of the mesh and the required physical fidelity.

2. Arbitrary Lagrange-Euler (ALE) Coupling Mechanics

The Arbitrary Lagrange-Euler (ALE) formulation is a hybrid methodology designed to manage material flow through moving meshes. In a standard Eulerian framework, the mesh is fixed; however, ALE allows the mesh grid points to move in synchronization with the Lagrangian structure's deformation.

At the interface, Lagrangian and Eulerian grid points coincide in physical space but remain logically distinct. As the structure deforms, the ALE motion algorithm propagates this movement through the Eulerian mesh. This allows material velocity relative to the moving mesh—a hallmark of Eulerian formulations—while accommodating structural shifts. A typical application is bird-strike analysis, where deformations are large but, crucially, smooth in time. ALE handles these interactions effectively only if the temporal transition of the interface is not erratic.

Strategic Limitations

Architects must be wary of two significant constraints when selecting ALE:

1. Solver Incompatibility: ALE is fundamentally incompatible with the Roe Solver. This is a critical limitation for high-speed gas dynamics where Riemann-based solvers are preferred for accuracy.
2. Material Constraints: It cannot be used with Eulerian single-material elements that possess strength.

3. High-Efficiency Fast Coupling Protocols

In simulation design, we frequently face a trade-off between the computational cost of general coupling and the performance of fast coupling. Fast coupling is the industry standard for production-level simulations due to its speed, provided the domain is strictly orthogonal.

Technical Requirements

To enable PARAM, FASTCOUP, four specific conditions must be satisfied:

1. Orthogonal Domain: The Euler domain must be defined via CHEXA or MESH, BOX entries aligned with the basic coordinate system axes.
2. Coupling Surface: A surface must be defined to encompass all structural segments interacting with the fluid.
3. Entry Definition: A COUPLE entry must reference this surface.
4. Activation: The PARAM, FASTCOUP instruction must be present in the input file.

The Closed Volume Constraint

Fast coupling requires the coupling surface to be a logically "closed volume" with no holes or T-joints. If a geometry, such as an open bunker (Example EP4_7) or a tank with internal baffles, naturally includes these features, the architect must manually mesh the openings with "dummy segments." These segments ensure the volume is closed, but the manual effort is significant—often requiring multiple coupling surfaces and Euler domains to represent "inside" and "outside" fluids separately.

Comparison: General vs. Fast Coupling

Feature	General Coupling	Fast Coupling
Mesh Geometry	Supports non-orthogonal meshes	Requires orthogonal meshes
Computational Cost	High (Expensive recalculations)	Low (High-efficiency protocols)
Surface Requirements	Flexible surface definition	Requires closed volumes / no holes
Implementation	Default COUPLE	Activated via PARAM, FASTCOUP

4. The Auto Coupling Paradigm: Barriers and Sub-Elements

When geometric complexity renders manual dummy-segment creation unfeasible, we turn to Auto Coupling (PARAM, AUTOCOUP). This paradigm redefines the coupling surface: it is no longer a "container" separating interior/exterior regions, but a "barrier" to fluid flow. Note that PARAM, AUTOCOUP cannot be combined with PARAM, FASTCOUP.

Sub-Elements and Orthogonal Projection

Auto Coupling manages "holes" by splitting parent Euler elements into "Sub-Elements." When a structure ends within an element, the algorithm automatically creates dummy segments to close the loop within that element. This is illustrated by the Plate with Hole scenario: the algorithm takes free edges (Points A and B) and performs an orthogonal projection to the opposing Euler faces (Points C and D). This ensures a closed loop for the sub-element calculation without requiring the user to mesh the entire global hole.

Expert Warnings and Limitations

While versatile, Auto Coupling is a sophisticated and occasionally fragile method. It is not suitable for folded air bag simulations. Other limitations include:

* Self-Intersections: The coupling surface cannot intersect itself.
* Splitting Limits: A single Euler element cannot be split into more than three sub-elements.
* Output Visibility: By default, Euler elements intersected by the structure show zero values in archives. To see actual sub-element values, the architect must use PARAM, AUTOCOUP, OUTPUT.

5. Modeling Porosity and Material Flow Between Domains

Porosity is essential for simulating semi-permeable membranes. It is important to distinguish between environmental interaction and domain-to-domain flow.

* Environmental Leakage: Handled via PORFLOW, which models interaction between an Eulerian region and the external ambient environment.
* Domain-to-Domain Flow: Managed via PORFCPL or PORFLCPL.

Pressure Method vs. Velocity Method

* Pressure Method (PORFCPL): Based on the pressure difference between the Euler gas and a target domain. This is restricted to ideal gases (Gamma Law EOS) and is intended for small holes using isentropic expansion.
* Velocity Method (PORFLCPL): Based on the velocity of the gas relative to the moving coupling surface. This is the preferred method for general applications.

Technical Procedure for Flow Activation

1. Associate a unique Euler domain with each of the two coupling surfaces.
2. Define a subsurface of elements shared by both surfaces to represent the hole.
3. Define a COUPOR entry referencing the subsurface and the porosity model.
4. Specify the target coupling surface in the PORFLCPL/PORFCPL entry to bridge the domains.

Calculation Methods: POLPACK vs. FACET

POLPACK (default) is the most accurate method, subdividing facets to connect exactly one Euler element in the first domain to one in the second. FACET is an approximate averaging method required only when Euler elements were generated externally (e.g., in Patran) rather than via the MESH entry.

6. Specialized Fluid-Filled Container (FFCONTR) Modeling

For quasi-static scenarios like the axial loading of plastic bottles, a full multi-material Euler solution is "quite expensive" and often unnecessary. The FFCONTR option provides a high-efficiency alternative.

Uniform Pressure and Hotfilling

FFCONTR assumes the fluid is incompressible and the gas above it obeys ideal gas laws. As the container deforms, volume changes translate directly into pressure changes. In "Hotfilling" simulations, fluid volume is temperature-dependent; users must provide density-versus-temperature tables.

Architect’s Note: The "Initial Pressure" specified in FFCONTR is used for volume-pressure curve calculation. It does not replace boundary condition forces. If an over-pressure exists (e.g., carbonation), it must be modeled with a PLOAD, which is then superimposed on the FFCONTR pressure.

7. Solver Optimization, Accuracy, and Troubleshooting

The Roe Solver and Temporal Integration

The Roe Solver is the state-of-the-art for gas dynamics, utilizing Riemann problem solutions at element faces.

* Entropy Fix: This ensures expansion shocks are correctly broken into expansion fans, preventing physically impossible entropy decreases.
* Spatial Accuracy: 1st-order accuracy uses a 1-stage Runge-Kutta scheme. 2nd-order accuracy (recommended for blast waves) uses a 3-stage scheme and the MUSCL scheme with a TVD limiter to prevent spurious oscillations.

Efficiency and Subcycling

Geometric updates are computationally taxing. By activating COSUBCYC, the geometry is only updated based on motion threshold. The COSUBMAX parameter further controls this frequency, significantly reducing overhead in large-scale models.

Technical Troubleshooting: Triangulation and Shifts

Auto Coupling often fails when structural segments lie exactly on Euler element faces, resulting in "Joint type not implemented" or "Dummy surface cannot be triangulated" errors.

* The Workaround: Slightly shifting the Euler mesh or geometric coordinates (e.g., from -1.5 to -1.501) is a standard architectural fix. This forces structural segments into the interior of Euler elements, facilitating successful triangulation and resolving free-edge warnings.

Summary of Methodology Selection

* Fast Coupling: Prioritize for simple, orthogonal geometries where speed is paramount and the volume can be closed.
* ALE Coupling: Select for large, smooth structural deformations (e.g., bird-strike) where the Roe Solver is not required.
* Auto Coupling: Use for complex, open geometries with T-joints where manual dummy segments are not feasible.

Technical Reference: Application-Specific Default Settings and Configuration Hierarchy

1. Introduction to Application-Driven Configuration

In the domain of high-fidelity simulation, the strategic implementation of application-specific defaults is a critical lever for optimizing engineering workflows. These predefined configuration profiles are designed to govern the delicate equilibrium between computational throughput and physical fidelity. By employing standardized application settings, engineers can ensure that numerical algorithms are pre-calibrated to the specific physical phenomena of a given study, thereby reducing manual setup errors and ensuring consistent solver behavior across complex projects.

This architectural framework categorizes simulations into six primary application types, each dictating a unique set of numerical defaults:

* STANDARD: The baseline configuration serving as the general-purpose benchmark for standard structural analyses.
* CRASH: Optimized for high-energy impact scenarios and vehicle safety evaluations.
* SHEETMETAL: Tailored for the complexities of metal forming, specifically addressing bending and stretching gradients.
* SPINNING: Engineered to accommodate the unique inertial dynamics of fast-rotating structures.
* FAST: Prioritizes solution velocity and reduction of CPU overhead, occasionally at the expense of absolute numerical precision.
* VERSION2: A legacy profile that maintains numerical parity with software versions prior to 3.0.

These profiles provide the foundational logic for element formulations and constitutive behavior. The following analysis dissects the specific algorithmic adjustments triggered by these profiles to ensure optimal solver performance.


--------------------------------------------------------------------------------


2. Comparative Analysis of Application Profiles

Specialized engineering challenges demand distinct numerical treatments; the requirements for capturing the transient dynamics of a vehicle crash differ fundamentally from the steady-state rotation of a turbine or the localized deformation in a stamping die. The following profiles dictate how the solver initializes element formulations, manages hourglassing, and processes material plasticity.

STANDARD

Element Formulation Standard configurations utilize Belytschko-Lin-Tsay (BLT) shell elements as the default. These elements typically employ three integration points through the thickness to provide a balanced response for general structural loading. Solid elements default to one-point Gauss integration via the PSOLID entry.

Hourglass Suppression Method

* Shells: Flanagan-Belytschko Stiffness (FBV) with a warping coefficient of 0.1. Rigid body rotation correction is inactive.
* Solids: Flanagan-Belytschko Stiffness (FBS).

Material Plasticity Behavior Plasticity is governed by a standard iterative scheme, which permits the solver to iterate until convergence is reached, capped at a maximum of 20 iterations.

CRASH

Element Formulation This profile utilizes BLT shell elements with three integration points through the thickness. To capture large deformation physics, element thickness is strain-dependent. Transverse shear stresses are assumed constant, and no specific mechanisms are active to avoid shear-locking.

Hourglass Suppression Method

* Shells: FBV method (warping coefficient 0.1, no rotation correction).
* Solids: Flanagan-Belytschko Stiffness (FBS).

Material Plasticity Behavior Employs the iterative plasticity scheme with a 20-iteration limit to ensure stability during high-velocity impact calculations.

FAST

Element Formulation To maximize computational speed, this profile employs a "fast" BLT shell formulation. While it retains three integration points, it dictates a constant element thickness, ignoring strain-dependency to reduce the per-cycle calculation cost.

Hourglass Suppression Method

* Shells: FBV method (warping coefficient 0.1, no rotation correction).
* Solids: Flanagan-Belytschko Stiffness (FBS).

Material Plasticity Behavior Standard iterative scheme (max 20 iterations).

SHEETMETAL

Element Formulation Similar to the CRASH profile, SHEETMETAL utilizes BLT shells and strain-dependent thickness. However, it increases the through-thickness resolution to five integration points. This is a critical adjustment for capturing the complex bending gradients and localized thinning characteristic of metal forming.

Hourglass Suppression Method

* Shells: FBV method (warping coefficient 0.1, no rotation correction).
* Solids: Flanagan-Belytschko Stiffness (FBS).

Material Plasticity Behavior Uses the iterative scheme (max 20 iterations). Note that specialized material models, such as SHEETMAT, may supersede this default with their own non-iterative algorithms.

SPINNING

Element Formulation The SPINNING profile departs from BLT formulations in favor of Key-Hoff elements. These utilize three integration points and strain-dependent thickness. Crucially, transverse shear stresses are computed with a linear distribution, and shear-locking is actively avoided to maintain accuracy in high-centrifugal-force environments.

Hourglass Suppression Method

* Shells: Dyna method; the warping coefficient is set to zero, and rigid body rotation correction is active to handle the rotational frames.
* Solids: Original Dyna suppression method.

Material Plasticity Behavior Standard iterative scheme (max 20 iterations).

VERSION2

Element Formulation This legacy profile utilizes Bely (original Dyna Belytschko-Lin-Tsay) elements. It assumes constant element thickness and constant transverse shear stress, providing a stable but less refined approximation compared to modern BLT implementations.

Hourglass Suppression Method

* Shells: FBV method (warping coefficient 0.1, no rotation correction).
* Solids: Original Dyna suppression method.

Material Plasticity Behavior Unlike all other profiles, VERSION2 utilizes a one-step radial scale-back scheme for material plasticity, ensuring backward compatibility with legacy models.


--------------------------------------------------------------------------------


3. Global and Property-Specific Implementation

The configuration architecture is designed for strategic flexibility, allowing for a "Global-Local" governance model. This is achieved via the SETTING entry, which allows engineers to define a universal environment while exempting specific components that require specialized numerical treatment.

The SETTING entry utilizes Set IDs (SID) to group definitions and Property IDs (PID) to target specific geometry.

$ Global environment set to CRASH for the entire assembly (SID 1)
SETTING, 1, CRASH

$ Local override: Apply SPINNING defaults to a specific cooling fan (PID 2)
SETTING, 2, SPINNING, SHELL, 2


In this implementation, the global solver environment is governed by CRASH parameters. However, the shell elements associated with PID 2 (the cooling fan) are directed to use SPINNING formulations. This dual-layer definition is vital for modeling complex assemblies, such as a high-speed rotating turbine housed within a vehicle engine bay during a crash. Without this local control, "numerical pollution" could occur, where a global setting optimized for impact might destabilize or inaccurately represent the physics of the rotating component.


--------------------------------------------------------------------------------


4. Hierarchy of the Configuration Scheme

To maintain consistency within complex input decks, the software adheres to a rigid hierarchical order. This hierarchy ensures that explicit user intents at the property level always supersede broad global settings. When the solver encounters conflicting element formulations, it resolves them according to the following priority (lowest to highest):

1. SETTING: Application-level defaults (the global environment).
2. PARAM, SHELLFORM: Global parameter overrides that apply to all elements regardless of the SETTING entry.
3. PSHELL1 / PCOMPA: Property-specific definitions, representing the most granular level of control.

Parameter-Driven Overrides and Exceptions

The PARAM entry allows for wide-scale modification of application-sensitive defaults:

* PARAM, SHTHICK, NO: This dictates that all element thicknesses remain strain-independent. It overrides every application type except SHEETMETAL, which maintains its strain-dependent thickness due to the critical nature of thinning in forming analysis.
* PARAM, SHPLAST: This allows the user to manually select the plasticity algorithm (RAD, VECT, or ITER). This setting governs all applications except VERSION2, which is hard-coded to maintain its radial scale-back (RADIAL) method for legacy consistency.

Hourglass Control Dominance

The HGSUPPR entry holds a unique status within this hierarchy. If an HGSUPPR entry is defined, it prevails over all other hourglass definitions, whether they were established by a global SETTING or a property-level default. This ensures that when an engineer explicitly defines a suppression method to combat instability, the solver honors that command above all automated profiles.

This hierarchical structure empowers the user to maintain total control over numerical algorithms, ensuring that specific manual overrides are respected even when broad application profiles are active.
