# coding: utf-8
##
##  Free Group
##
#------------------------------------------------------------
class Letter
  #---
  def initialize(char='1')
    '''
      Argument: [1a-zA-Z]
    '''
    raise ArgumentError, "You can use alphabet and '1'" unless char[0] =~ /[1a-zA-Z]/
    @char = char[0].downcase
    @sign = (char[0] == @char) ? 1 : -1
  end
  attr_reader :char
  #---
  def =~(a_Letter)
    raise ArgumentError unless a_Letter.is_a? Letter
    @char == a_Letter.char
  end
  def ==(a_Letter)
    raise ArgumentError unless a_Letter.is_a? Letter
    (self =~ a_Letter) && (self.inverse? == a_Letter.inverse?)
  end
  def ===(a_Letter)
    raise(ArgumentError) unless a_Letter.is_a? Letter
    self.object_id == a_Letter.object_id
  end
  def <=>(a_Letter)
    raise(ArgumentError) unless a_Letter.is_a? Letter
    self.show <=> another.show
  end
  #---
  def to_s
    (@sign == 1) ? @char : @char.upcase
  end
  def show() self.to_s end
  #---  
  def inverse
    if @char == '1' then
      self.dup
    else
      self.class.new((@sign == 1) ? @char.upcase : @char)
    end
  end
  def inverse?() (@char == '1') ? nil : (@sign == 1) end
  def inverse_of?(a_Letter)
    (@char == '1') ? (a_Letter.char == '1') : (self =~ a_Letter) && (self.sign != a_Letter.sign)
  end
end

#------------------------------------------------------------
class Word < Array
  #---
  # Word class which is a (nested) array of Letters.
  #---
  def initialize(*args)
    args.flatten!
    args.each do |arg|
      self << case arg
               when Letter then
                 arg
               when String then
                  arg.each_char.map{|c| Letter.new(c)} unless arg.empty?
               else
                  raise ArgumentError, arg.class
               end
    end
    self << Letter.new if self.empty?
    self.flatten! if self.size == 1 && self[0].is_a?(Array)
  end
  #---
  def letter_at(int) (self.flatten)[int] end
  def first_letter() (self.flatten).first end
  def last_letter() (self.flatten).last end
  #---
  def count(a_letter)
    a_letter = Letter.new(a_letter) if a_letter.is_a?(String)
    return (self.flatten).count(a_letter)
  end
  #---
  def split(num)
    raise ArgumentError unless ( num.is_a?(Integer) && (0..self.size).include?(num) )
    div = (num == 0) ? [Letter.new, self] : [self[0..num-1], self[num..-1]]
    return div.map{|sub| self.class.new(sub)}
  end     
  #---
  def show() show_parens(self).gsub(/[()]+/, '.').gsub(/^[.]|[.]$/, '') end 
  def show_parens(myarr)
    myarr.map{|f| (f.is_a? Array) ? "(#{self.show_parens(f)})" : f.show }.join
  end
  #---
  def inverse() self.class.new((self.flatten).reverse.map(&:inverse)) end
  #---
  def deep_copy
    str_arr = self.map{|letter| letter.to_s}
    return self.class.new(str_arr)
  end
  #---
  def contract_once
    arr = self.dup
    if arr.size > 1
      left, right = self.class.new, arr.flatten
      while right.size > 1
        left *= right.shift
        if left.last.inverse == right.first
          left.pop
          right.shift
        end
      end
      left *= right
    end
    return left
  end
  def contract
    w = self.dup
    size_diff = 1
    while (size_diff > 0 && w.size > 1)
      before = w.size
      w = w.contract_once
      after = w.size
      size_diff = before - after
    end
    return w
  end
  #---
  def cyclic_permutation(num=1)
    self.class.new((self.flatten).rotate(num))
  end
  def cyclic_reduce
    ww = (self.dup).contract 
    wcp = self.class.new
    while (wcp.size < ww.size)
      ww = wcp unless wcp.show == '1'
      wcp = ww.cyclic_permutation.contract
    end
    return ww
  end
  def is_cyclically_same?(aWord)
    words = [self, aWord].map(&:cyclic_reduce)
    (0..words[0].size-1).each do |i|
        if (words[0].cyclic_permutation(i) == words[1])
          return true
          break
        end
    end
    return false
  end
  #---
  def *(anElement)
    letters = self.map{|v| v}
    case anElement
    when Letter
      letters << anElement
    when Word
      letters += anElement  #NOTE: As a result, the variable letters is an Array.
    else
      raise ArgumentError, anElement.class
    end
    letters.delete(Letter.new)
    return (letters.empty?) ? Word.new : self.class.new(letters)
  end
  def ^(idx)
    raise ArgumentError unless (idx.is_a?(Integer) and idx >= 0)    
    return idx.times.map{|k| self}.inject{|pd, w| pd*w}
  end
end
      
#------------------------------------------------------------
module Group extend self
  Identity = Word.new('1')
  #---
  def product(element1,element2)
    words = to_word(element1, element2)
    return words[0]*words[1]
  end
  def commutator(element1, element2)
    words = to_word(element1, element2)
    return words[0]*words[1]*(words[0].inverse)*(words[1].inverse)
  end
  def conjugate(element1, element2)
    words = to_word(element1, element2)
    return words[1]*words[0]*(words[1].inverse)
  end
  private
  def to_word(*elements)
    raise ArgumentError unless elements.all?{|elm| (elm.is_a? Word) || (elm.is_a? Letter)}
    elements.map{|elm| (elm.is_a? Word) ? elm : Word.new(elm)}
  end
end