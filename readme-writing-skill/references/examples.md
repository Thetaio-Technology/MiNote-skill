# Examples

## Example 1: Typora line break to GitHub line break

Before:

```md
<div align="center">
**把你的小米云笔记接入ai agent**
**让Ai更靠近你一点**
</div>
```

After:

```md
<div align="center">
**把你的小米云笔记接入ai agent**

<br/>

**让Ai更靠近你一点**
</div>
```

## Example 2: Blockquote paragraph separation

Before:

```md
> ⚙️ **`minote-driver`** 负责在底层啃硬骨头，**把事做成**。
> 🪄 **`minote-skill`** 负责在上层做封装，**让这事更好调用**。
```

After:

```md
> ⚙️ **`minote-driver`** 负责在底层啃硬骨头，**把事做成**。
>
> 🪄 **`minote-skill`** 负责在上层做封装，**让这事更好调用**。
```

## Example 3: Image scaling compatible with GitHub

Before:

```html
<img src="./assest/img1.jpg" alt="小米的便签板.jpg|300" style="zoom:30%;" />
```

After:

```html
<img src="./assest/img1.jpg" alt="小米的便签板" width="30%" />
```

## Example 4: AI-sounding bullet list to formal prose

Before:

```md
这个仓库更适合：

- 对外展示 skill 能力
- 承载 agent 集成文档
- 承载机器可读 manifest
- 作为从 `minote-driver` 同步发布出来的 skill 仓库
- 在单仓库内完成 skill 安装与执行
```

After:

```md
该仓库用于集中提供 `minote-skill` 的能力说明、集成文档与机器可读清单，并作为与 [`minote-driver`](https://github.com/Thetaio-Technology/MiNote-driver) 对应发布的 skill 仓库，支持在单一仓库内完成安装、配置与执行。
```

## Example 5: Broken link correction

Before:

```md
[`minote-driver`](https://github.com/thetaio/minote-driver.git)
```

After:

```md
[`minote-driver`](https://github.com/Thetaio-Technology/MiNote-driver)
```
