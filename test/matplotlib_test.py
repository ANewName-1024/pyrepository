import matplotlib.pyplot as plt
import matplotlib.patches as patches

def create_diagram(filename, title, boxes, connections):
    plt.rcParams['font.family'] = 'SimHei'  # 替换为你选择的字体
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    for x, y, w, h, text in boxes:
        rect = patches.Rectangle((x, y), w, h, fill=False)
        ax.add_patch(rect)
        ax.text(x + w/2, y + h/2, text, ha="center", va="center")

    for (x1, y1, x2, y2) in connections:
        ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle="->"))

    ax.set_title(title)
    plt.savefig(filename, bbox_inches="tight")
    plt.show()
    plt.close()

if __name__ == '__main__':
    # Diagram 1: FX AI Framework
    create_diagram(
        "fx_ai_framework.png",
        "AI 外汇监管体系框架图",
        [
            (4, 8, 2, 1, "应用层"),
            (4, 6, 2, 1, "模型层"),
            (4, 4, 2, 1, "数据层"),
            (4, 2, 2, 1, "风险控制层")
        ],
        [(5, 8, 5, 7), (5, 6, 5, 5), (5, 4, 5, 3)]
    )
    # Diagram 2: Workflow
    create_diagram(
        "fx_ai_workflow.png",
        "AI 外汇智能审核流程图",
        [
            (1, 8, 3, 1, "资料上传"),
            (6, 8, 3, 1, "单证识别"),
            (1, 5, 3, 1, "一致性校验"),
            (6, 5, 3, 1, "风险评分"),
            (3.5, 2, 3, 1, "审核建议输出")
        ],
        [
            (4, 8.5, 6, 8.5),
            (2.5, 8, 2.5, 6),
            (7.5, 8, 7.5, 6),
            (4, 5, 6, 5),
            (2.5, 5, 4, 3)
        ]
    )
    # Diagram 3: Risk Logic
    create_diagram(
        "fx_ai_risklogic.png",
        "AI 风险评分逻辑结构图",
        [
            (1, 7, 3, 1, "客户行为数据"),
            (6, 7, 3, 1, "交易特征"),
            (1, 4, 3, 1, "历史记录"),
            (6, 4, 3, 1, "模型计算"),
            (3.5, 1, 3, 1, "风险等级输出")
        ],
        [
            (2.5, 7, 2.5, 5),
            (7.5, 7, 7.5, 5),
            (2.5, 4, 4, 2),
            (7.5, 4, 4, 2)
        ]
    )
