-- clean-math-v4.lua
-- LLM-friendly cleanup for Pandoc LaTeX->Markdown output.
-- - Normalize theorem-like blocks to headers
-- - Remove anchor-only label paragraphs
-- - Rewrite cross-references using consistent prefixes (assump:..., sec:..., etc.)
-- Bibliography preserved.

local env_titles = {
  theorem = "Theorem",
  lemma = "Lemma",
  proposition = "Proposition",
  corollary = "Corollary",
  definition = "Definition",
  assumption = "Assumption",
  remark = "Remark",
  example = "Example",
  proof = "Proof"
}

local prefix_titles = {
  assump = "Assumption",
  thm    = "Theorem",
  lemma  = "Lemma",
  prop   = "Proposition",
  cor    = "Corollary",
  def    = "Definition",
  sec    = "Section",
  eq     = "Equation",
  fig    = "Figure",
  tab    = "Table",
  alg    = "Algorithm"
}

local function has_attr(el, key, val)
  if not el.attributes then return false end
  if val == nil then return el.attributes[key] ~= nil end
  return el.attributes[key] == val
end

local function split_prefix(ref)
  if not ref then return nil, nil end
  local p, rest = string.match(ref, "^([%w%-]+)%:([%w%-%._]+)$")
  return p, rest
end

local function pretty_ref(ref)
  local p, rest = split_prefix(ref)
  if p and rest then
    local title = prefix_titles[p] or (p:sub(1,1):upper() .. p:sub(2))
    return title .. " (" .. rest .. ")"
  end
  return ref
end

function Para(el)
  if #el.content == 1 then
    local c = el.content[1]
    if c.t == "Span" then
      local sp = c
      if (sp.identifier ~= nil and sp.identifier ~= "") and (#sp.content == 0) then
        return {}
      end
      if (#sp.content == 0) and has_attr(sp, "reference-type") then
        return {}
      end
    end
    if c.t == "Link" then
      local lk = c
      if (#lk.content == 0) then
        return {}
      end
    end
  end
  return nil
end

function Div(el)
  for _, cls in ipairs(el.classes) do
    local t = env_titles[cls]
    if t then
      local blocks = {}
      table.insert(blocks, pandoc.Header(4, pandoc.Inlines({ pandoc.Str(t) })))
      for _, b in ipairs(el.content) do
        table.insert(blocks, b)
      end
      return blocks
    end
  end
  return nil
end

function Link(el)
  local ref = nil
  if el.attributes then
    ref = el.attributes["reference"] or el.attributes["ref"] or el.attributes["data-reference"]
  end
  if not ref and el.target and type(el.target) == "string" then
    if el.target:sub(1,1) == "#" then
      ref = el.target:sub(2)
    end
  end

  local is_ref = has_attr(el, "reference-type", "ref") or has_attr(el, "reference-type") or (ref ~= nil)

  if is_ref and ref then
    return pandoc.Inlines({ pandoc.Str(pretty_ref(ref)) })
  end

  if el.attributes then
    el.attributes["reference-type"] = nil
    el.attributes["reference"] = nil
    el.attributes["label"] = nil
  end
  return nil
end

function Span(el)
  if has_attr(el, "reference-type") or has_attr(el, "reference") or has_attr(el, "label") then
    el.attributes["reference-type"] = nil
    el.attributes["reference"] = nil
    el.attributes["label"] = nil
    if (el.identifier ~= nil and el.identifier ~= "") and (#el.content == 0) then
      return {}
    end
    return el
  end
  return nil
end
