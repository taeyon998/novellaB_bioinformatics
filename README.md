# novellaB_bioinformatics
My work as an undergraduate research assistant under professor Hongyi Xin in UMJI_SJTU.

##Task
1. Simulate and plot a "Median UMIs per cell vs. Raw Reads per cell" graph.  
      Language: MATLAB  
      Objective: See how many raw reads are needed to see at least x reads per UMI  
      Criteria:   
        -Generate random RNA data (eg. 1024 molecules per UMI, 30 UMIs in total)  
        -Apply capture rate 0.2%, which is the standard capture rate used nowadays for sc-RNA sequencing (2020)  
        -See how many molecules were captured for each UMI (eg. 3 reads for 1st UMI, 1 read for 2nd UMI...)  
        -Plot 2D graph, average reads per UMI vs reads (total captured molecules)  
        
2. Plot the Binomial Distribution for "Number of captured UMIs per cell for different capture rates & number of copies"  
      Language: Python  
      Objective: See how likely it is to get at least N reads per UMI, given a capture rate and number of copies per UMI.   
                  Biologists could use this model to adjust the (1) PCR rate or (2) the capture rate in the sequencing machine.  
      Criteria:  
          -Plot a 3D graph, (x reads per UMI, capture rate r) vs. probability of capturing x molecules)  
          -Receive user input: (1) number of UMI, (2) number of molecules per UMI, (3) different capture rates  
 
