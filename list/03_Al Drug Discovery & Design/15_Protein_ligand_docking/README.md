# 分子对接方案的改进

## 1. 调整了代码 - 15_Protein_ligand_docking_latest.ipynb

### 改进的地方 

- 持久化状态：通即使脚本中断，下次运行时也可以继续处理未完成的对接任务
2. 检查已处理的任务：在process_docking函数中，首先检查当前的PDB和SMILES组合是否已经处理过，如果已经处理过，则跳过该任务，这样子几不用再次操作了

3. 实时保存结果到CSV，就是害怕突然断开了，没有数据，做了一个实时保存结果的功能，





# Improvement of molecular docking scheme

# # 1. Adjusted the code-15 _ Protein _ ligand _ docking _ latest.ipynb
# # # # Improvements
- Persistence state: Even if the script is interrupted, you can continue to process unfinished docking tasks at the next run.
- Check the processed tasks: In the process_docking function, first check whether the current PDB and SMILES combination has been processed. If it has been processed, skip the task, so that there is no need to operate again.

- Save the results to CSV in real time, but I'm afraid of sudden disconnection and no data, so I made a real-time saving function of results.